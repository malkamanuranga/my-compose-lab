from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        db_host = os.getenv("DB_HOST", "unknown")
        message = f"Custom API is LIVE! Connected to database host: {db_host}"
        self.wfile.write(message.encode())

HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
