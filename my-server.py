from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self.do_HEAD()
        #print(self.wfile)
        self.wfile.write(b'<html><head><title>MyServer</title></head>')
        self.wfile.write(b'<h1>Yooo welcome</h1>')
        self.wfile.write(f'<p>You are on path: {self.path}</p>'.encode('utf-8'))


if __name__ == '__main__':
    try:
        server = HTTPServer(('localhost', 8080), MyServer)
        print('Starting server...')
        print('Access as http://localhost:8080')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Stopping the server')
        server.shutdown()
        