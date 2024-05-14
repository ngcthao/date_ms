# Based off of: https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
import socket
from datetime import date, timedelta
SERVER_IP = "127.0.0.1"
PORT = 8000
# Port to listen on (non-privileged ports are > 1023)


def get_date(x):
    try:
        today = date.today()
        selected_date = today + timedelta(days=int(x))
    except ValueError:
        return "0"
    else:
        return selected_date.strftime("%B %d, %Y")


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen(0)
    print(f"Listening on {SERVER_IP}:{PORT}")
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    try:
        while True:
            request = client_socket.recv(1024).decode("utf-8")

            if request.lower() == "exit":
                client_socket.send("closed".encode("utf-8"))
                break

            print(f"Received: {request}")

            response = get_date(request).encode("utf-8")
            client_socket.send(response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection to client closed")
        server.close()


run_server()