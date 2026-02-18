#!/usr/bin/env python3

import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # 🔹 Endpoint /data
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())

        # 🔹 Endpoint /status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 🔹 Gestion des erreurs (endpoint inconnu)
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            error_message = {
                "error": "Endpoint not found"
            }

            self.wfile.write(json.dumps(error_message).encode())


# 🔹 Lancement du serveur
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
