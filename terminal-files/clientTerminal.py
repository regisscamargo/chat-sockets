from config import *
import threading
import socket


class Client:
    def __init__(self, user, svr, prt):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (svr, int(prt))
        self.client.connect(ADDR)
        self.online = True

        self.name = user
        self.send_message(self.name)

        self.thread_recv = threading.Thread(target=self.receive_message, args=())
        self.thread_recv.start()
               
        self.main_loop()      


    def main_loop(self):
        '''Loop principal do cliente, aguarda o usuário digitar uma mensagem e envia para o servidor'''
        while self.online:
            try:
                msg = str(input())
                if msg != "" and msg != DISCONNECT_MESSAGE:
                    self.send_message(msg)
                    msg = ""
                else:
                    self.disconnect()
                    self.online = False
            except: 
                self.disconnect()


    def send_message(self, msg):
        '''Envia mensagens para o servidor'''
        try:
            message, send_length = encode_message(msg)
            self.client.send(send_length)
            self.client.send(message)

            if msg == DISCONNECT_MESSAGE:
                self.disconnect()

        except:
            print("Falha na conexão")
            self.online = False


    def receive_message(self):
        '''Recebe mensagens do servidor e as imprime no terminal'''
        while self.online:
            try:
                msg_length = self.client.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = self.client.recv(msg_length).decode(FORMAT)
                    print(msg)
            except:
                self.online = False


    def disconnect(self):
        '''Desconecta o cliente do servidor'''
        # Encerrando conexão socket
        print("Você está se desconectando...")
        self.client.close()
        self.online = False
        print("[CONEXÃO ENCERRADA]")
    


def encode_message(msg):
    '''Codifica a mensagem para envio ao servidor'''
    message = str(msg).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    return message, send_length


    

if __name__ == "__main__":
    print("========== Chat dos Gurizes Terminal ==========\n")
    
    username = input("Insira seu nome: ")
    
    c = Client(username, SERVER, PORT)
