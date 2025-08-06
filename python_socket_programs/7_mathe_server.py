import socket

def evaluate_expression(expr):
    try:
        return str(eval(expr))
    except:
        return "Invalid Expression"

server_socket = socket.socket()
server_socket.bind(('localhost', 12346))
server_socket.listen(1)
print("Calculator Server Ready...")

conn, addr = server_socket.accept()
expr = conn.recv(1024).decode()
result = evaluate_expression(expr)
conn.send(result.encode())
conn.close()