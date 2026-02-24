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
            
            ytt_api = YouTubeTranscriptApi()
            transcript = None
            error_msg = None
            
            # Try to fetch with different languages
            for langs in [['ko'], ['en'], ['ja'], ['ko', 'en', 'ja']]:
                try:
                    transcript = ytt_api.fetch(video_id, languages=langs)
                    break
                except Exception as e:
                    error_msg = str(e)
                    continue
            
            # Try without language preference
            if not transcript:
                try:
                    transcript = ytt_api.fetch(video_id)
                except Exception as e:
                    error_msg = str(e)
            
            if not transcript:
                self.wfile.write(json.dumps({'error': error_msg or 'No transcript available'}).encode())
                return
            
            # Format result - transcript entries have .start and .text attributes
            result = [{'start': entry.start, 'text': entry.text} for entry in transcript]
            self.wfile.write(json.dumps(result).encode())
            
        except ImportError as e:
            self.wfile.write(json.dumps({'error': f'Import error: {str(e)}'}).encode())
        except Exception as e:
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
