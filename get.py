from http.server import BaseHTTPRequestHandler, HTTPServer

data = [
    {
        "Name": "Samuel",
        "Track": "AI Developer"
    }
]
class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 200):
        self.send_response(status)
        self.send_header()