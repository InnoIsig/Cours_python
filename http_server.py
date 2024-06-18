import http.server
import socketserver

port = 800
adress = ("", port)

# sever = http.server.HTTPServer

handler = http.server.SimpleHTTPRequestHandler

# handler = http.server.CGIHTTPRequestHandler
httpd = socketserver.TCPServer(adress, handler)
# handler.cgi_directories = ["/"]

print(f"Serveur démaré sur le port {port}")

httpd.serve_forever()