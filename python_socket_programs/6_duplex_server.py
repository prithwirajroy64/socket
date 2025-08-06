import socket
import threading

def receive(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print("Client:", msg)
        except:
            break

server = socket.socket()
server.bind(('localhost', 12348))
server.listen(1)
print("Waiting for client...")
conn, addr = server.accept()
print("Connected with", addr)

threading.Thread(target=receive, args=(conn,), daemon=True).start()

while True:
    msg = input("You: ")
    conn.send(msg.encode())