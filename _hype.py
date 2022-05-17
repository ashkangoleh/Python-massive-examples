from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import re

hostName = "0.0.0.0"
serverPort = 8088


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if None != re.search('/api/', self.path):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes("<html><head><title>Ashkan</title></head>", "utf-8"))
            self.wfile.write(bytes(f"<p>Request:{self.path}</p>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(
                bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("Not found", "utf-8"))
        


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server Started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server Terminated.")
