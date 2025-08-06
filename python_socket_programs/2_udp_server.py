import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server is listening...")

while True:
    data, addr = server_socket.recvfrom(1024)
    message = data.decode()
    count = len(message)
    server_socket.sendto(str(count).encode(), addr)