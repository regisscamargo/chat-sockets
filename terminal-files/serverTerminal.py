import threading
import socket
from datetime import datetime

import socket
import threading
from datetime import datetime

HEADER_LENGTH = 64
PORT_NUMBER = 5050
SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())
SERVER_INFO = (SERVER_ADDRESS, PORT_NUMBER)
MESSAGE_FORMAT = 'utf-8'
DISCONNECT_COMMAND = "!DISCONNECT"
NEW_MESSAGE_COMMAND = "!NEW_MESSAGE"

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.server_socket.bind(SERVER_INFO)
        self.connected_clients = []
        self.client_usernames = []
        self.server_online = True
        print("========== Chat dos Gurizes Terminal ==========\n")
        print("Inicializando servidor...")
        self.server_socket.listen()
        print(f"[LISTENING] Server is listening on {SERVER_ADDRESS} port {PORT_NUMBER}")
        self.accept_clients()

    def accept_clients(self):
        '''Aceita conexões de clientes e cria uma nova thread para cada cliente conectado'''
        while self.server_online:
            try:
                client_socket, client_address = self.server_socket.accept()
                username = self.receive_username(client_socket)
                self.add_client(client_socket, username)
                thread = threading.Thread(target=self.listen_client, args=(client_socket, username))
                thread.start()
                self.notify_client_connection(username)
            except Exception as e:
                print(f"[ERROR] {e}")
                print("[CLOSING] Server is closing.")
                self.server_socket.close()
                self.server_online = False
                return

    def receive_username(self, client_socket):
        '''Recebe o nome de usuário do cliente conectado'''
        username_length = int(client_socket.recv(HEADER_LENGTH).decode(MESSAGE_FORMAT))
        username = client_socket.recv(username_length).decode(MESSAGE_FORMAT)
        return username

    def add_client(self, client_socket, username):
        '''Adiciona o cliente conectado à lista de clientes ativos'''
        self.client_usernames.append(username)
        self.connected_clients.append(client_socket)

    def disconnect_client(self, client_socket, username):
        '''Remove um cliente da lista de clientes ativos'''
        index = self.connected_clients.index(client_socket)
        self.client_usernames.pop(index)
        self.connected_clients.remove(client_socket)
        client_socket.close()
        self.notify_client_disconnection(username)

    def listen_client(self, client_socket, username):
        '''Escuta as mensagens enviadas pelo cliente conectado'''
        while True:
            try:
                message_length = client_socket.recv(HEADER_LENGTH).decode(MESSAGE_FORMAT)
                if message_length:
                    message_length = int(message_length)
                    message = client_socket.recv(message_length).decode(MESSAGE_FORMAT)
                    if message == DISCONNECT_COMMAND:
                        self.disconnect_client(client_socket, username)
                        return
                    self.handle_message(message, client_socket, username)
            except Exception as e:
                print(f"[ERROR] {e}")
                self.disconnect_client(client_socket, username)
                return

    def handle_message(self, message, client_socket, username):
        '''Trata as mensagens recebidas do cliente conectado'''
        if message == NEW_MESSAGE_COMMAND:
            self.broadcast_message(message, client_socket, username)

    def broadcast_message(self, message, client_socket, username):
        '''Envia mensagens para todos os clientes conectados, exceto para o cliente que enviou a mensagem'''
        timestamp = self.get_timestamp()
        formatted_message = f"{username} ({timestamp}): {message}"
        print(formatted_message)
        encoded_message = self.encode_message(formatted_message)
        for client in self.connected_clients:
            if client != client_socket:
                client.send(encoded_message[1])
                client.send(encoded_message[0])

    def notify_client_connection(self, username):
        '''Notifica os clientes conectados sobre a entrada de um novo cliente'''
        message = f"{username} entrou no chat. Conexões ativas {len(self.connected_clients)}."
        self.broadcast_message(message, None, "Servidor")

    def notify_client_disconnection(self, username):
        '''Notifica os clientes conectados sobre a saída de um cliente'''
        timestamp = self.get_timestamp()
        message = f"{username} saiu do chat ({timestamp})."
        self.broadcast_message(message, None, "Servidor")

    def get_timestamp(self):
        '''Retorna a data e hora atuais no formato dd/mm/aaaa - hh:mm:ss'''
        now = datetime.now()
        return now.strftime("%d/%m/%Y - %H:%M:%S")

    def encode_message(self, message):
        '''Codifica a mensagem para envio ao cliente conectado'''
        encoded_message = message.encode(MESSAGE_FORMAT)
        message_length = len(encoded_message)
        send_length = str(message_length).encode(MESSAGE_FORMAT)
        send_length += b' ' * (HEADER_LENGTH - len(send_length))
        return encoded_message, send_length

if __name__ == "__main__":
    server = Server()
