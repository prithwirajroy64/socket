import socket

def perform_operation(operation, num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == 'add':
            return str(num1 + num2)
        elif operation == 'sub':
            return str(num1 - num2)
        elif operation == 'mul':
            return str(num1 * num2)
        elif operation == 'div':
            if num2 == 0:
                return "Error: Division by zero"
            return str(num1 / num2)
        else:
            return "Error: Invalid operation"
    except ValueError:
        return "Error: Invalid numbers"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")


client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

data = client_socket.recv(1024).decode()
if not data:
  client_socket.send("Error: Invalid operation".encode())

parts = data.split()
if len(parts) != 3:
    response = "Error: Format must be <operation> <num1> <num2>"
else:
    operation, num1, num2 = parts
    response = perform_operation(operation, num1, num2)

client_socket.send(response.encode())
client_socket.close()
