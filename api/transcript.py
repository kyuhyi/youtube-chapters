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
            from youtube_transcript_api.formatters import JSONFormatter
            
            transcript = None
            error_msg = None
            
            # Try different language codes
            lang_codes = ['ko', 'en', 'en-US', 'ja', 'zh-Hans', 'es', 'de', 'fr']
            
            for lang in lang_codes:
                try:
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                    transcript = transcript_list.find_transcript([lang]).fetch()
                    break
                except Exception as e:
                    error_msg = str(e)
                    continue
            
            # If no specific language found, try to get any available transcript
            if not transcript:
                try:
                    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                    # Get first available transcript
                    for t in transcript_list:
                        transcript = t.fetch()
                        break
                except Exception as e:
                    error_msg = str(e)
            
            # Last resort: try direct fetch
            if not transcript:
                try:
                    transcript = YouTubeTranscriptApi.get_transcript(video_id)
                except Exception as e:
                    error_msg = str(e)
            
            if not transcript:
                self.wfile.write(json.dumps({'error': error_msg or 'No transcript available'}).encode())
                return
            
            # Format result
            result = [{'start': entry['start'], 'text': entry['text']} for entry in transcript]
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
