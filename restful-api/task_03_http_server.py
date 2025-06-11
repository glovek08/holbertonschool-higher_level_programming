#!/usr/bin/python3
"""
Hosts a basic HTTP server, defines POST and GET requests
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import json


HOST = "localhost"
PORT = 8000


class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))
        #throwing json info on info endpoint
        elif self.path == "/info":
            try:
                json_output = json.dumps({"version": "1.0", 
                    "description": "A simple API built with http.server"})
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_output.encode("utf-8"))
            except Exception as error:
                print(error)
                self.send_error(500, f"Server error: {error}")
                HTTPError
        # accessing /data endpoint
        elif self.path == '/data':
            try:
                json_output = json.dumps(
                    {"name": "John", "age": 30, "city": "New York"})
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json_output.encode("utf-8"))
            except Exception as error:
                print(f"Error in JSON stuff: {error}")
                self.send_error(500, f"Server error: {error}")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", "utf-8"))

my_server = HTTPServer((HOST, PORT), NeuralHTTP)
# print("Server ON...")
my_server.serve_forever()
my_server.server_close()
# print("Server CLOSED.")
