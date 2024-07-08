import maya.cmds as cmds
import http.server
import json
import threading

class MayaHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/frame':
            current_frame = cmds.currentTime(query=True)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Allow CORS
            self.end_headers()
            self.wfile.write(json.dumps({'frame': current_frame}).encode())
        else:
            self.send_error(404)

    def log_message(self, format, *args):
        # Silence console output
        return

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MayaHTTPRequestHandler)
    print(f"Maya HTTP Server running on port {port}")
    httpd.serve_forever()

server_thread = None

def start_server(port=8000):
    global server_thread
    if server_thread is None or not server_thread.is_alive():
        server_thread = threading.Thread(target=run_server, args=(port,))
        server_thread.daemon = True
        server_thread.start()
        print(f"Maya HTTP Server started on port {port}")
    else:
        print("Server is already running")

def stop_server():
    global server_thread
    if server_thread and server_thread.is_alive():
        # This will only stop the server in newer Python versions
        # In older versions, you might need to restart Maya to fully stop the server
        http.server.HTTPServer.shutdown(http.server.HTTPServer)
        server_thread.join()
        print("Maya HTTP Server stopped")
    else:
        print("No server is running")

# Usage in Maya:
# start_server()
# stop_server()