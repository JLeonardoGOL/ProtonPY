import socket

def handle_request(request):
    if request.startswith("GET /ruta1"):
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Ruta 1</h1>"

    elif request.startswith("GET /ruta2"):
        return "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Ruta 2</h1>"

    else:
        return "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>Página no encontrada</h1>"

def server():
    host = "127.0.0.1"
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor local http://{host}:{port}")

    while True:
        client_connection, client_address = server_socket.accept()
        data = client_connection.recv(1024).decode()

        if data:
            response = handle_request(data)
            client_connection.sendall(response.encode())

        client_connection.close()

server()
