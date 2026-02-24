from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import urllib.request

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
            # Use YouTube Innertube API (internal API)
            innertube_url = 'https://www.youtube.com/youtubei/v1/get_transcript'
            
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept-Language': 'ko-KR,ko;q=0.9,en;q=0.8'
            }
            
            # Innertube request body
            body = json.dumps({
                "context": {
                    "client": {
                        "clientName": "WEB",
                        "clientVersion": "2.20240101.00.00"
                    }
                },
                "params": self._get_transcript_params(video_id)
            }).encode('utf-8')
            
            req = urllib.request.Request(innertube_url, data=body, headers=headers)
            
            try:
                with urllib.request.urlopen(req, timeout=10) as response:
                    data = json.loads(response.read().decode('utf-8'))
                    
                    # Parse transcript from Innertube response
                    result = self._parse_innertube_response(data)
                    if result:
                        self.wfile.write(json.dumps(result).encode())
                        return
            except Exception as e:
                pass  # Fall through to timedtext method
            
            # Fallback: Try direct timedtext API
            for lang in ['ko', 'en', 'ja', 'a.ko', 'a.en']:
                try:
                    timedtext_url = f'https://www.youtube.com/api/timedtext?v={video_id}&lang={lang}&fmt=json3'
                    req = urllib.request.Request(timedtext_url, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    })
                    
                    with urllib.request.urlopen(req, timeout=10) as response:
                        captions = json.loads(response.read().decode('utf-8'))
                        
                        result = []
                        for event in captions.get('events', []):
                            if 'segs' in event:
                                start = event.get('tStartMs', 0) / 1000
                                text = ''.join(seg.get('utf8', '') for seg in event['segs'])
                                if text.strip():
                                    result.append({'start': start, 'text': text.strip()})
                        
                        if result:
                            self.wfile.write(json.dumps(result).encode())
                            return
                except:
                    continue
            
            self.wfile.write(json.dumps({
                'error': 'Could not fetch transcript. YouTube may be blocking cloud IPs. Please use manual transcript input.'
            }).encode())
            
        except Exception as e:
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def _get_transcript_params(self, video_id):
        import base64
        # Encode video ID for transcript request
        param = f'\n\x0b{video_id}'
        return base64.b64encode(param.encode()).decode()
    
    def _parse_innertube_response(self, data):
        try:
            actions = data.get('actions', [])
            for action in actions:
                transcript_body = action.get('updateEngagementPanelAction', {}).get(
                    'content', {}).get('transcriptRenderer', {}).get(
                    'body', {}).get('transcriptBodyRenderer', {})
                
                cue_groups = transcript_body.get('cueGroups', [])
                result = []
                
                for group in cue_groups:
                    cues = group.get('transcriptCueGroupRenderer', {}).get('cues', [])
                    for cue in cues:
                        cue_data = cue.get('transcriptCueRenderer', {})
                        start_ms = int(cue_data.get('startOffsetMs', 0))
                        text_runs = cue_data.get('cue', {}).get('simpleText', '')
                        
                        if not text_runs:
                            runs = cue_data.get('cue', {}).get('runs', [])
                            text_runs = ''.join(r.get('text', '') for r in runs)
                        
                        if text_runs.strip():
                            result.append({
                                'start': start_ms / 1000,
                                'text': text_runs.strip()
                            })
                
                if result:
                    return result
        except:
            pass
        return None

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
