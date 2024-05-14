# Based off of: https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
# import socket
SERVER_IP = "127.0.0.1"
PORT = 8000
# Port to listen on (non-privileged ports are > 1023)


def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    try:
        while True:
            msg = input("Enter message: ")
            if msg == "":
                msg = "0"
            client.send(msg.encode("utf-8")[:1024])
            response = client.recv(1024).decode("utf-8")

            if response.lower() == "closed":
                break

            print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed.")


run_client()
