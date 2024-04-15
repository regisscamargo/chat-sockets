from config import *
import threading
import logging
class Client():

    def __init__(self, server, username, conn):
        '''Construtor da classe ChatClient.'''
        self.server = server
        self.username = username 
        self.conn = conn 
        self.clientOnline = True

        thread = threading.Thread(target=self.startListening, args=())
        thread.start()

    def startListening(self):
        '''Função que inicia a escuta do servidor.'''
        logging.info('[LISTENING] Server is listening for messages')
        while self.clientOnline and self.server.online:
            try:
                msgLength = self.conn.recv(HEADER).decode(FORMAT) 
                if msgLength: 
                    msgLength = int(msgLength) 
                    msg = self.conn.recv(msgLength).decode(FORMAT) 
                    self.handleMessage(msg)
                
            except: 
                self.server.unsubscribe(self)
                self.clientOnline = False
                return
    
    def handleMessage(self, msg):
        '''Função que trata as mensagens recebidas pelo servidor.'''
        logging.info('[MESSAGE] Server received a message')
        op = msg[0]
        msgContent = msg[1:]

        if (op == NEW_MESSAGE):
            self.server.globalMsg(msgContent, self)
        
        elif (op == CHANGE_NAME):
            notification = f"{NEW_MESSAGE}<p><i>***<b>{self.username}</b> alterou seu nome para <b>{msgContent}</b>.***</i></p>"
            self.server.serverMsg(notification)
            self.username = msgContent
            self.server.userListUpdate()

        elif (op == DISCONNECT_MESSAGE): 
            self.clientOnline = False 
            self.server.unsubscribe()  

    def broadcast_message(self, message, client_socket, username):
        logging.info('[BROADCAST] Server is broadcasting message')
        '''Envia mensagens para todos os clientes conectados, exceto para o cliente que enviou a mensagem'''
        timestamp = self.get_timestamp()
        formatted_message = f"{username} ({timestamp}): {message}"
        print(formatted_message)
        encoded_message = self.encode_message(formatted_message)
        for client in self.connected_clients:
            if client != client_socket:
                client.send(encoded_message[1])
                client.send(encoded_message[0])
