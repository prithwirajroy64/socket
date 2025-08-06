import socket
from datetime import datetime

server = socket.socket()
server.bind(('localhost', 12349))
server.listen(1)
print("Time server running...")

conn, addr = server.accept()
while True:
    request = conn.recv(1024).decode()
    if request.lower() == 'time':
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.send(now.encode())
    elif request.lower() == 'exit':
        break

conn.close()