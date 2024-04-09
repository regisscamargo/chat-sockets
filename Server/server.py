import threading
import socket
from datetime import datetime

from serverClient import Client
from config import *

class Server():

    def __init__(self):
       
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.serverSocket.bind((SERVER, PORT))
        self.clients = []
        self.online = True

        print("========== Chat dos Gurizes Terminal ==========\n")
        print("Inicializando servidor...")
        
        self.serverSocket.listen()
        print(f"[LISTENING] Server is listening on {SERVER} port {PORT}")

        exitThread = threading.Thread(target=self.closeServer, args=())
        exitThread.start()

        self.subscribe()

    def subscribe(self):
       
        while self.online:
            try:
                conn, addr = self.serverSocket.accept()

                usernameLength = int(conn.recv(HEADER).decode(FORMAT))
                username = conn.recv(usernameLength).decode(FORMAT)

                client = Client(self, username, conn)
                self.clients.append(client)

                self.userListUpdate()

                currentDate = getCurrentDate()
                notificationMsg = f"{NEW_MESSAGE}<p><i>***{username} entrou no chat ({currentDate}). Conexões ativas {len(self.clients)}.***</i></p>"
                self.serverMsg(notificationMsg)
 
            except:
                print("[CLOSING] Server is closing.")
                self.serverSocket.close()
                self.online = False
                return

    def unsubscribe(self, client):
        
        self.clients.remove(client)
        client.conn.close()
 
        currentDate = getCurrentDate()
        notificationMsg = (f"{NEW_MESSAGE}<p><i>***{client.username} saiu do chat ({currentDate}). Conexões ativas {len(self.clients)}.***</i></p>")
        self.serverMsg(notificationMsg)

        self.userListUpdate()

    def serverMsg(self, msg):

        message, sendLength = encodeMsg(msg)

        for client in self.clients:       
            client.conn.send(sendLength)
            client.conn.send(message)

    def globalMsg(self, msg, client):

        currentDate = getCurrentDate()

        msgAll = (f"<p><u>{client.username}</u> ({currentDate}):<br>{msg}</p>")
        msgSelf = (f"<p><b>Eu ({currentDate}):</b><br>{msg}</p>")
        
        msgAll = (f"{NEW_MESSAGE}{msgAll}")
        msgSelf = (f"{NEW_MESSAGE}{msgSelf}")

        message, sendLength = encodeMsg(msgAll)
        messageSelf, sendLengthSelf = encodeMsg(msgSelf)

        for c in self.clients:
            if(c.conn != client.conn):
                c.conn.send(sendLength)
                c.conn.send(message)
            else:
                c.conn.send(sendLengthSelf)
                c.conn.send(messageSelf)

    def userListUpdate(self):

        for c in self.clients:
            message, sendLength = encodeMsg(f"{CLEAR_LIST}")            
            c.conn.send(sendLength)
            c.conn.send(message)

            for client in self.clients:
                if(c.conn == client.conn):
                    message, sendLength = encodeMsg(f"{NAME_LIST}{client.username} (Você)")
                else:
                    message, sendLength = encodeMsg(f"{NAME_LIST}{client.username}")
                c.conn.send(sendLength)
                c.conn.send(message)

    def closeServer(self):
        
        input("Pressione [ENTER] para encerrar o servidor\n")

        self.online = False
        self.serverSocket.close()


def getCurrentDate():
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    return(f"{now.day}/{now.month}/{now.year} - {currentTime}")

def encodeMsg(msg):
    message = str(msg).encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    return message, sendLength

if ("__main__" == __name__):
    server = Server()
