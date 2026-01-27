#!/usr/bin/env python3
"""Simple backend server for YouTube chapter generator"""

import http.server
import json
import os
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class ChapterHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # API endpoint for transcript
        if parsed.path == '/api/transcript':
            query = urllib.parse.parse_qs(parsed.query)
            video_id = query.get('videoId', [None])[0]
            
            if not video_id:
                self.send_error(400, 'Missing videoId')
                return
            
            try:
                from youtube_transcript_api import YouTubeTranscriptApi
                api = YouTubeTranscriptApi()
                
                # Try different languages
                transcript = None
                for lang in ['ko', 'en', 'en-US', 'ja']:
                    try:
                        transcript = api.fetch(video_id, languages=[lang])
                        break
                    except:
                        continue
                
                if not transcript:
                    # Try without language preference (get any available)
                    try:
                        transcript = api.fetch(video_id)
                    except Exception as e:
                        self.send_json(400, {'error': str(e)})
                        return
                
                # Format transcript
                result = [{'start': entry.start, 'text': entry.text} for entry in transcript]
                self.send_json(200, result)
                
            except ImportError:
                self.send_json(500, {'error': 'youtube-transcript-api not installed. Run: pip3 install youtube-transcript-api'})
            except Exception as e:
                self.send_json(400, {'error': str(e)})
            return
        
        # Serve static files
        return super().do_GET()
    
    def send_json(self, code, data):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    port = 8080
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('', port), ChapterHandler)
    print(f'🚀 YouTube Chapter Generator running at http://localhost:{port}')
    print('   Press Ctrl+C to stop')
    server.serve_forever()
