import socket
import threading

clients = []  # Daftar semua klien yang terhubung

def broadcast(message, sender_conn):
    """Fungsi untuk meneruskan pesan ke semua klien kecuali pengirim."""
    for client in clients:
        conn, addr = client
        if conn != sender_conn:  # Jangan kirim kembali ke pengirim
            try:
                conn.send(message)
            except Exception as e:
                print(f"Error saat mengirim pesan ke {addr}: {e}")
                conn.close()
                clients.remove(client)

def handle_client(conn, addr):
    """Fungsi untuk menangani komunikasi dengan setiap klien."""
    print(f"Terhubung ke {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"{addr}: {data}")
            
            # Meneruskan pesan ke klien lain
            broadcast(data, conn)

        except Exception as e:
            print(f"Terjadi error: {e}")
            break
    conn.close()
    print(f"Putus koneksi dengan {addr}")
    clients.remove((conn, addr))

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen()
    print("Server berjalan dan mendengarkan pada port 65432")

    while True:
        conn, addr = server_socket.accept()
        clients.append((conn, addr))  # Tambahkan klien ke daftar
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
