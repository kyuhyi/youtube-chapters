#!/usr/bin/env python3
"""Local server for YouTube chapter generator - bypasses cloud IP blocks"""

import http.server
import json
import os
import sys
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Fix encoding for Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

class ChapterHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # API endpoint for transcript
        if parsed.path == '/api/transcript':
            query = urllib.parse.parse_qs(parsed.query)
            video_id = query.get('videoId', [None])[0]
            
            if not video_id:
                self.send_json(400, {'error': 'Missing videoId'})
                return
            
            try:
                from youtube_transcript_api import YouTubeTranscriptApi
                
                api = YouTubeTranscriptApi()
                transcript = None
                error_msg = None
                
                # Try with different languages
                for langs in [['ko'], ['en'], ['ja'], ['ko', 'en', 'ja']]:
                    try:
                        transcript = api.fetch(video_id, languages=langs)
                        break
                    except Exception as e:
                        error_msg = str(e)
                        continue
                
                # Try without language preference
                if not transcript:
                    try:
                        transcript = api.fetch(video_id)
                    except Exception as e:
                        error_msg = str(e)
                
                if not transcript:
                    self.send_json(400, {'error': error_msg or 'No transcript available'})
                    return
                
                # Format transcript - entries have .text and .start attributes
                result = [{'start': entry.start, 'text': entry.text} for entry in transcript]
                self.send_json(200, result)
                
            except ImportError:
                self.send_json(500, {'error': 'youtube-transcript-api not installed. Run: pip install youtube-transcript-api'})
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
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Simple logging
        print(f"[{self.log_date_time_string()}] {args[0]}")

if __name__ == '__main__':
    port = 8081
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print()
    print('=' * 50)
    print('YouTube Chapter Generator - Local Server')
    print('=' * 50)
    print(f'Server running at http://localhost:{port}')
    print()
    print('Usage:')
    print(f'  Open http://localhost:{port} in your browser')
    print()
    print('Press Ctrl+C to stop')
    print('=' * 50)
    print()
    
    server = HTTPServer(('', port), ChapterHandler)
    server.serve_forever()
