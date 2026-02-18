#!/usr/bin/python3

import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """
        Gestionnaire de requêtes personnalisé pour notre API.
        Supporte les routes /, /data et /status.
    """
    def do_GET(self):
        """Gère les requêtes de type GET et distribue vers les endpoints."""
        # Route: Root /
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Route: /data
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # We use json.dumps to turn the dict into a string, then encode to bytes
            self.wfile.write(json.dumps(data).encode())

        # Route: /status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Route: 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Using 'allow_reuse_address' helps avoid "Address already in use" errors if you restart quickly
socketserver.TCPServer.allow_reuse_address = True

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            httpd.server_close()
