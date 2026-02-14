from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(b'Hello from onboarding sample app')
        else:
            super().do_GET()

if __name__ == '__main__':
    port = 8080
    print(f"Starting server on :{port}")
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()
