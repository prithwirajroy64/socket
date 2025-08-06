import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print("Enter operation in format: add|sub|mul|div number1 number2")
message = input("Enter your calculation: ")

client_socket.send(message.encode())

result = client_socket.recv(1024).decode()
print("Result from server:", result)

client_socket.close()
