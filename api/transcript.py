from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import urllib.request
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        video_id = query.get('videoId', [None])[0]
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        if not video_id:
            self.wfile.write(json.dumps({'error': 'Missing videoId'}).encode())
            return
        
        try:
            # Fetch YouTube video page
            url = f'https://www.youtube.com/watch?v={video_id}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
            }
            
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')
            
            # Extract captions data from ytInitialPlayerResponse
            pattern = r'ytInitialPlayerResponse\s*=\s*({.+?});'
            match = re.search(pattern, html)
            
            if not match:
                # Try alternative pattern
                pattern = r'"captions":\s*({.+?"captionTracks".+?})'
                match = re.search(pattern, html)
                if match:
                    captions_data = json.loads('{' + match.group(1) + '}')
                else:
                    self.wfile.write(json.dumps({'error': 'Could not find captions data'}).encode())
                    return
            else:
                player_response = json.loads(match.group(1))
                captions_data = player_response.get('captions', {})
            
            caption_tracks = captions_data.get('playerCaptionsTracklistRenderer', {}).get('captionTracks', [])
            
            if not caption_tracks:
                self.wfile.write(json.dumps({'error': 'No captions available for this video'}).encode())
                return
            
            # Find Korean or English captions
            caption_url = None
            for track in caption_tracks:
                lang = track.get('languageCode', '')
                if lang in ['ko', 'en', 'ja']:
                    caption_url = track.get('baseUrl')
                    if lang == 'ko':
                        break
            
            if not caption_url:
                caption_url = caption_tracks[0].get('baseUrl')
            
            if not caption_url:
                self.wfile.write(json.dumps({'error': 'Could not find caption URL'}).encode())
                return
            
            # Fetch captions XML
            caption_url += '&fmt=json3'
            req = urllib.request.Request(caption_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                captions_json = json.loads(response.read().decode('utf-8'))
            
            # Parse captions
            result = []
            for event in captions_json.get('events', []):
                if 'segs' in event:
                    start = event.get('tStartMs', 0) / 1000
                    text = ''.join(seg.get('utf8', '') for seg in event['segs'])
                    if text.strip():
                        result.append({'start': start, 'text': text.strip()})
            
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
