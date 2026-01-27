from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

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
            from youtube_transcript_api import YouTubeTranscriptApi
            api = YouTubeTranscriptApi()
            
            transcript = None
            for lang in ['ko', 'en', 'en-US', 'ja', 'es']:
                try:
                    transcript = api.fetch(video_id, languages=[lang])
                    break
                except:
                    continue
            
            if not transcript:
                try:
                    transcript = api.fetch(video_id)
                except Exception as e:
                    self.wfile.write(json.dumps({'error': str(e)}).encode())
                    return
            
            result = [{'start': entry.start, 'text': entry.text} for entry in transcript]
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
