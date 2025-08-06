import socket

'''
Create a TCP socket
socket.AF_INET: IPv4 address family.
socket.SOCK_STREAM: TCP (reliable, connection-oriented).
This creates a client-side socket that will connect to a server.
'''
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
Connect to the server
Connects to a server running on the same machine (localhost) and port 12345.
This should match the server's bind() address.
'''
client_socket.connect(('localhost', 12345))
'''
Take input from the user
Prompts the user to enter a message.
Stores it in the message variable as a string.
'''
message = input("Enter message: ")
'''
Send the message to the server
encode() converts the string message to bytes, which are required for network communication.
send() transmits the message to the connected server.
'''
client_socket.send(message.encode())
'''
Receive response from the server
recv(1024) reads up to 1024 bytes from the server.
decode() converts the received bytes back into a string.
In this case, it's expected to be the same message (echo).
'''
response = client_socket.recv(1024).decode()
print("Echo from server:", response)
# Close the connection
client_socket.close()

'''
step 1: first `import socket` korte hobe

step 2: socket create er jonne bolte hobe j ip version ki aur TCP no UDP

step 3: clint k server er sathe connect korte hole ekta address and r server er port ta ek sathe connect korte hbe -> client_socket.connect(('localhost', 12345))

step 4: message = input("Enter message: ")

step 5: server k message ta send korte hbe

step 6: client_socket.send(message.encode())

step 7: erpr jodi server kichu send kore tahole seta amader store korte hbe 

step 8: response = client_socket.recv(1024).decode()

step 9: last e client socket ta close korte hbe -> client_socket.close()
'''