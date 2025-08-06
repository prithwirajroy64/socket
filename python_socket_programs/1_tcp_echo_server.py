import socket

'''
Creating a TCP socket
socket.AF_INET: Specifies the address family for IPv4.
socket.SOCK_STREAM: Indicates a TCP socket (reliable, connection-based).
server_socket: This is the socket object that represents the server.
'''
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
Binding the socket to an address and port
Binds the server socket to localhost on port 12345.
This means the server will listen only for connections on the local machine at that port.
'''
server_socket.bind(('localhost', 12345))
'''
Start listening for incoming connections
listen(1) puts the server into listening mode, allowing it to accept 1 connection at a time.
It waits for a client to connect.
'''
server_socket.listen(1)
print("Server is listening on port 12345...")

'''
Accepting a client connection
accept() waits (blocking) until a client connects.
It returns a new socket (conn) for communication and the client's address (addr).
'''
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
'''
Receiving data from the client
recv(1024) receives up to 1024 bytes of data from the client.
.decode() converts the received bytes to string.
'''
data = conn.recv(1024).decode()
print("Received:", data)
'''
Sending the same data back to the client
This is an echo response: it sends back the same data.
encode() converts the string back to bytes before sending.
'''
conn.send(data.encode())
# Closing the connection
conn.close()



'''
step 1: first `import socket` korte hobe

step 2: socket create er jonne bolte hobe j ip version ki aur TCP no UDP

step 3: ekta server/ clint ekta address and port thake seta amder eksathe
bind(server->bind/client->connect) korte hbe

step 4: set korte hbe j at a time server koto gulo client accept korbek

step 5: erpr asche client jodi request pathai

step 6: server_socket.accept() -> etar help niye amra client er sathe connection build korbo

step 7: ei function ta duta jinis return kore 1) ekta new connection and 2) client er address

step 8: oi duta k duta veriable a store korbo

step 9: jodi new connection(client) tai jodi kono message send kore

step 10: conn.recv(1024).decode() eitar help niye message ta `data` veriable er store korbo(1024 bytes)

step 11: clint k kono kichu send korar thakle ei bhabe pathabo -> conn.send(data.encode())

step 12: erpr amader connection ta close korte hbe -> conn.close()
'''