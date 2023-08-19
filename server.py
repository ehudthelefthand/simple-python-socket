import socket

# Define the server's IP address and port
server_ip = "0.0.0.0"  # Bind to all available network interfaces
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {server_ip}:{server_port}")

while True:
    # Accept a new client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    
    # Receive and print data from the client
    data = client_socket.recv(1024).decode("utf-8")
    print(f"Received data: {data}")
    
    # Send a response back to the client
    response = "Hello from the server!"
    client_socket.send(response.encode("utf-8"))
    
    # Close the client socket
    client_socket.close()