import socket

try:
    s = socket.socket()
    s.connect(("google.com", 80))
    print("Connected to google.com on port 80")
    s.close()
except Exception as e:
    print("Connection failed:", e)