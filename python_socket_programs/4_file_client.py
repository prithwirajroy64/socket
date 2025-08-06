import socket
import os

file_path = input("Enter full file path to send (only .txt file): ").strip()
if not os.path.isfile(file_path):
    print("!File does not exist.")
    exit()

file_name = os.path.basename(file_path)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5001))

client_socket.send(file_name.encode())

ack = client_socket.recv(1024).decode()
if ack != 'READY':
    print("!Server did not acknowledge.")
    client_socket.close()
    exit()

with open(file_path, "rb") as f:
    while True:
        bytes_read = f.read(1024)
        if not bytes_read:
            break
        client_socket.sendall(bytes_read)

print("File sent successfully.")
client_socket.close()
