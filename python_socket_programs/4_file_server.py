import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5001))
server_socket.listen(1)
print("Server is listening on port 5001...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

file_name = conn.recv(1024).decode()
print(f"Receiving file: {file_name}")

conn.send(b'READY')

with open("received_" + file_name, "wb") as f:
    while True:
        bytes_read = conn.recv(1024)
        if not bytes_read:
            break
        f.write(bytes_read)

print("File received successfully.")
conn.close()
server_socket.close()
