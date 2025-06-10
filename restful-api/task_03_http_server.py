#!/usr/bin/python3
"""
Hosts a basic HTTP server, defines POST and GET requests
"""
from http.server import HTTPServer, BaseHTTPRequestHandler


HOST = "192.168.1.90"
PORT = 8000

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

my_server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server ON...")
my_server.serve_forever()
my_server.server_close()
print("Server CLOSED.")