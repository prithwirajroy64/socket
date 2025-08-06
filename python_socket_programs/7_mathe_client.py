import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 12346))
expr = input("Enter expression (e.g., 3+5*2): ")
if any(char.isalpha() for char in expr):
  print("!invalid expression")
  exit()
client_socket.send(expr.encode())
print("Result:", client_socket.recv(1024).decode())
client_socket.close()