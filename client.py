import socket
from cipher import CaesarCipher, VignereCipher, SubstitutionCipher

cipher_suite = SubstitutionCipher() # Ganti sesuai dengan cipher yang ingin digunakan

def start_client(client_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65433))  # Menghubungkan ke MITM Proxy

    print(f"{client_name} terhubung ke MITM Proxy")

    stop_flag = threading.Event()

    def receive_messages():
        while not stop_flag.is_set():
            try:
                # Menerima pesan dari server
                data = client_socket.recv(1024)
                
                message = cipher_suite.decrypt(data).decode()
                
                if message:
                    print(f"\r{message}\n{client_name} > ", end='')  # Tetap tampilkan client_name >
                else:
                    break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    def send_messages():
        while not stop_flag.is_set():
            message = input(f"{client_name} > ")
            if message.lower() == 'exit':
                stop_flag.set()
                break
            
            encrypted_message = cipher_suite.encrypt(message.encode())
            
            client_socket.sendall(encrypted_message)

        client_socket.close()

    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

    receive_thread.join()
    send_thread.join()   

if __name__ == "__main__":
    import sys
    import threading
    if len(sys.argv) != 2:
        print("Usage: python client.py <ClientName>")
        sys.exit(1)
    client_name = sys.argv[1]
    start_client(client_name)

