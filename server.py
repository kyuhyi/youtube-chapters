#!/usr/bin/env python3
"""Local server for YouTube chapter generator - bypasses cloud IP blocks"""

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
                self.send_json(400, {'error': 'Missing videoId'})
                return
            
            try:
                from youtube_transcript_api import YouTubeTranscriptApi
                
                # Try different methods
                transcript = None
                error_msg = None
                
                # Method 1: List transcripts and find by language
                try:
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                    
                    # Try Korean first
                    for lang in ['ko', 'en', 'ja']:
                        try:
                            transcript = transcript_list.find_transcript([lang]).fetch()
                            break
                        except:
                            continue
                    
                    # Get any available
                    if not transcript:
                        for t in transcript_list:
                            transcript = t.fetch()
                            break
                except Exception as e:
                    error_msg = str(e)
                
                # Method 2: Direct fetch
                if not transcript:
                    try:
                        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko', 'en', 'ja'])
                    except:
                        try:
                            transcript = YouTubeTranscriptApi.get_transcript(video_id)
                        except Exception as e:
                            error_msg = str(e)
                
                if not transcript:
                    self.send_json(400, {'error': error_msg or 'No transcript available'})
                    return
                
                # Format transcript
                result = [{'start': entry['start'], 'text': entry['text']} for entry in transcript]
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

if __name__ == '__main__':
    port = 8081
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print()
    print('=' * 50)
    print('🚀 YouTube 챕터 생성기 로컬 서버')
    print('=' * 50)
    print(f'✅ http://localhost:{port} 에서 실행 중')
    print()
    print('📋 사용법:')
    print(f'   브라우저에서 http://localhost:{port} 열기')
    print()
    print('⏹️  종료: Ctrl+C')
    print('=' * 50)
    print()
    
    server = HTTPServer(('', port), ChapterHandler)
    server.serve_forever()
