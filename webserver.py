import os
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080
HOST = 'localhost'


class ServerHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.path = None

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except Exception as e:
            print(e)
            file_to_open = 'File not found: {}'.format(e)
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


def main():
    server = HTTPServer((HOST, PORT), ServerHandler)
    print('Server running at http://{}:{}'.format(HOST, PORT))
    server.serve_forever()


if __name__ == '__main__':
    main()
