import socket

server_ip = "127.0.0.1"  # Use the server's IP address
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

message = "Hello from the client!"
client_socket.send(message.encode("utf-8"))

response = client_socket.recv(1024).decode("utf-8")
print("Received response:", response)

client_socket.close()
