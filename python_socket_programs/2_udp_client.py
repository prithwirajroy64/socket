import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Enter message: ")
client_socket.sendto(msg.encode(), ('localhost', 12345))
count, _ = client_socket.recvfrom(1024)
print("Character count from server:", count.decode())
client_socket.close()