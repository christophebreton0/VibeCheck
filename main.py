from http.server import HTTPServer
from webserver import ServerHandle

PORT = 8080
HOST = 'localhost'


def main():
    server = HTTPServer((HOST, PORT), ServerHandle)
    print('Server running at http://{}:{}'.format(HOST, PORT))
    server.serve_forever()


if __name__ == '__main__':
    main()

