from http.server import SimpleHTTPRequestHandler, HTTPServer

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Serveur démarré sur http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run()from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class RequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()