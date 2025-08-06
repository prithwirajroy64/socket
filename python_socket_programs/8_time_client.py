import socket

client = socket.socket()
client.connect(('localhost', 12349))

while True:
    msg = input("Type 'time' to get server time or 'exit' to quit: ")
    client.send(msg.encode())
    if msg.lower() == 'exit':
        break
    print("Server Time:", client.recv(1024).decode())

client.close()