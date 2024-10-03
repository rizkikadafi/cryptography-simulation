# mitm.py
import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432
MITM_HOST = '127.0.0.1'
MITM_PORT = 65433

def handle_client(client_socket, server_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[MITM] Menerima data dari klien: {data}")
            server_socket.sendall(data)
        except:
            break
    client_socket.close()
    server_socket.close()

def handle_server(server_socket, client_socket):
    while True:
        try:
            data = server_socket.recv(1024)
            if not data:
                break
            print(f"[MITM] Menerima data dari server: {data}")
            client_socket.sendall(data)
        except:
            break
    server_socket.close()
    client_socket.close()

def start_mitm():
    mitm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mitm_socket.bind((MITM_HOST, MITM_PORT))
    mitm_socket.listen()
    print(f"MITM Proxy berjalan dan mendengarkan pada {MITM_HOST}:{MITM_PORT}")

    while True:
        client_socket, addr = mitm_socket.accept()
        print(f"Klien terhubung dari {addr}")

        # Terhubung ke server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((SERVER_HOST, SERVER_PORT))

        # Membuat dua thread untuk menangani komunikasi
        client_to_server = threading.Thread(target=handle_client, args=(client_socket, server_socket))
        server_to_client = threading.Thread(target=handle_server, args=(server_socket, client_socket))
        client_to_server.start()
        server_to_client.start()

if __name__ == "__main__":
    start_mitm()
