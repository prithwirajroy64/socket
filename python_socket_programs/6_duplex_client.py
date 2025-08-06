import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print("Server:", msg)
        except:
            break

client = socket.socket()
client.connect(('localhost', 12348))
threading.Thread(target=receive, args=(client,), daemon=True).start()

while True:
    msg = input("You: ")
    client.send(msg.encode())