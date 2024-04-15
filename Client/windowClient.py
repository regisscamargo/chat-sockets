import socket
import threading
import datetime
import logging
from config import *

class Client():
    def __init__(self, username, address, port, win):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ADDR = (address, int(port))
        self.client.connect(ADDR)
        self.username = username
        self.win = win
        self.online = True
        message, send_length = encodeMsg(self.username)
        self.client.send(send_length)
        self.client.send(message)
        self.thread_recv = threading.Thread(target=self.recvMsg, args=())
        self.thread_recv.start()

    def recvMsg(self):
        '''Recebe mensagens do servidor e as envia para o método handleMsg'''
        logging.info('[LISTENING] Server is listening for messages')
        while self.online:
            try:
                msg_lenght = self.client.recv(HEADER).decode(FORMAT)
                if msg_lenght:
                    msg_lenght = int(msg_lenght)
                    msg = self.client.recv(msg_lenght).decode(FORMAT)
                    self.handleMsg(msg)
            except:
                self.online = False

    def send_data(self, data):
        '''Envia dados para o servidor'''
        logging.info('[SENDING] Client is sending data')
        self.client.send(data)

    def broadcast_message(self, message, client_socket):
        '''Envia mensagens para todos os clientes conectados, exceto para o cliente que enviou a mensagem'''
        logging.info('[BROADCAST] Server is broadcasting message')
        timestamp = self.get_timestamp()
        formatted_message = f"({timestamp}): Enviou um arquivo com nome: {message}"
    
    def get_timestamp(self):
        '''Retorna a data e hora atuais no formato dd/mm/aaaa - hh:mm:ss'''
        logging.info('[TIMESTAMP] Getting timestamp')
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y - %H:%M:%S")
    
    def handleMsg(self, msg):
        '''Trata as mensagens recebidas do servidor e as envia para a interface gráfica'''
        logging.info('[MESSAGE] Server received a message')
        op = msg[0]
        msg_list = list(msg)
        msg_list.pop(0)
        msg = "".join(msg_list)
        if op == NEW_MESSAGE:
            self.win.signal.chatLabel.emit(msg)
        elif op == CLEAR_LIST:
            self.win.signal.listUser.emit('')
        elif op == NAME_LIST:
            self.win.signal.listUser.emit(msg)

    def sendMsg(self, msg, op):
        '''Envia mensagens para o servidor'''
        logging.info('[SENDING] Client is sending message')
        if self.online:
            try:
                msg = op + msg
                message, send_length = encodeMsg(msg)
                self.client.send(send_length)
                self.client.send(message)
            except:
                self.disconnect()

    def disconnect(self):
        '''Desconecta o cliente do servidor'''
        logging.info('[DISCONNECT] Client is disconnecting')
        if self.online:
            self.win.signal.chatLabel.emit("<p><i>Você está se desconectando...</i><p>")
            message, send_length = encodeMsg(DISCONNECT_MESSAGE)
            self.client.send(send_length)
            self.client.send(message)
            self.online = False
            self.client.close()
            self.win.signal.chatLabel.emit("<p><i><b>[CONEXÃO ENCERRADA]</i></p>")

def encodeMsg(msg):
    '''Codifica a mensagem para envio ao servidor'''
    logging.info('[ENCODE MESSAGE] Encoding message')
    message = str(msg).encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    return message, send_length
