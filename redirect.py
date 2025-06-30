from http.server import BaseHTTPRequestHandler, HTTPServer

website = "examplesite.com"

class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        host = self.headers.get("Host",website)
        self.send_response(301)
        self.send_header('Location',f'https://{host}{self.path}')
        self.end_headers()

redirect = HTTPServer(('',80),Redirect)


print('redirect server started')


try:
    redirect.serve_forever()
except KeyboardInterrupt:
    pass


redirect.server_close()
