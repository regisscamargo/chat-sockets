import sys
from config import *
from windowClient import Client
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import os
import datetime


class MySignal(QtCore.QObject):
    listUser = QtCore.pyqtSignal(str)
    chatLabel = QtCore.pyqtSignal(str)

class MainWindow(QMainWindow):
    def __init__(self, username, address, port):
        super(QMainWindow, self).__init__()
        self.signal = MySignal()
        self.signal.listUser.connect(self.listUpdate)
        self.signal.chatLabel.connect(self.chatUpdate)
        self.client = Client(username, address, port, self)
        self.setupUi()

    def setupUi(self):
        '''Configura a interface gráfica'''
        self.setWindowIcon(QtGui.QIcon(u"img\\miniLogo.png"))
        self.setObjectName("MainWindow")
        self.resize(850, 600)
        self.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(200, 200))
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        self.logo.setSizeIncrement(QtCore.QSize(400, 400))
        self.logo.setBaseSize(QtCore.QSize(150, 151))
        self.logo.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(u"img\\logo.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(False)
        self.logo.setIndent(-2)
        self.logo.setObjectName("logo")
        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("background-color: white;")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.gridLayout.addWidget(self.titulo, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)    
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: white;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.userList = QtWidgets.QTextBrowser(self.centralwidget)
        self.userList.setMinimumSize(QtCore.QSize(200, 100))
        self.userList.setMaximumSize(QtCore.QSize(250, 500))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.userList.setFont(font)
        self.userList.setStyleSheet("background-color: gray;")
        self.userList.setObjectName("userList")
        self.gridLayout.addWidget(self.userList, 4, 0, 1, 1)
        self.msg = QtWidgets.QLineEdit(self.centralwidget)
        self.msg.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.msg.setFont(font)
        self.msg.setStyleSheet("background-color: gray;")
        self.msg.setObjectName("msg")
        self.gridLayout.addWidget(self.msg, 6, 2, 1, 1)
        self.chat = QtWidgets.QTextBrowser(self.centralwidget)
        self.chat.setMinimumSize(QtCore.QSize(300, 400))
        self.chat.setMaximumSize(QtCore.QSize(4000, 4000))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.chat.setFont(font)
        self.chat.setStyleSheet("background-color: gray;")
        self.chat.setObjectName("chat")
        self.gridLayout.addWidget(self.chat, 0, 2, 5, 2)
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.sendBtn.setSizePolicy(sizePolicy)
        self.sendBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sendBtn.setObjectName("sendBtn")
        self.gridLayout.addWidget(self.sendBtn, 6, 3, 1, 1)
        self.sendBtn.clicked.connect(self.newMsg)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setStyleSheet("background-color: rgb(192, 192, 192);")  # Cinza
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.actionChangeName = QtWidgets.QAction(self)
        self.actionChangeName.setObjectName("actionChangeName")
        self.actionLimpar = QtWidgets.QAction(self)
        self.actionLimpar.setObjectName("actionLimpar")
        self.actionEncerrarConn = QtWidgets.QAction(self)
        self.actionEncerrarConn.setObjectName("closeConn")
        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.menuSobre = QtWidgets.QAction(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        self.menuOptions.addAction(self.actionChangeName)
        self.menuOptions.addAction(self.actionEncerrarConn)
        self.menuOptions.addAction(self.actionLimpar)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionQuit)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuSobre)
        self.setCentralWidget(self.centralwidget) 
        self.translateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def translateUi(self):
        '''Traduz os textos da interface gráfica'''
        _translate = QtCore.QCoreApplication.translate
        self.msg.setPlaceholderText(_translate("self", u"Escreva uma mensagem", None))
        self.setWindowTitle(_translate("MainWindow", "Chat dos Gurizes"))
        self.titulo.setText(_translate("MainWindow", "Chat dos Gurizes"))
        self.menuOptions.setTitle(_translate("MainWindow", "Menu"))
        self.actionChangeName.setText(_translate("MainWindow", "Alterar Nome"))
        self.actionEncerrarConn.setText(_translate("MainWindow", "Encerrar Conexão"))
        self.actionLimpar.setText(_translate("MainWindow", "Limpar Chat"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.menuSobre.setText(_translate("MainWindow", "Enviar arquivo"))
        self.label.setText(_translate("MainWindow", "Usuários Conectados"))
        self.sendBtn.setText(_translate("MainWindow", "Enviar"))
        self.actionChangeName.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionEncerrarConn.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionLimpar.setShortcut(_translate("MainWindow", "Escape"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionChangeName.triggered.connect(self.changeNameWin)
        self.actionEncerrarConn.triggered.connect(self.client.disconnect)
        self.actionLimpar.triggered.connect(self.chat.clear)
        self.actionQuit.triggered.connect(self.closeEvent)
        self.menuSobre.triggered.connect(self.sobreWin)

    def newMsg(self):
        '''Envia uma nova mensagem para o servidor'''
        msg = self.msg.text()
        if msg:
            self.client.sendMsg(msg, NEW_MESSAGE)
            self.msg.setText('')

    def changeNameWin(self):
        '''Abre uma janela para alterar o nome do usuário'''
        self.nameWin = QMainWindow()
        self.nameWin.setWindowIcon(QtGui.QIcon(u"img\\miniLogo.png"))
        self.nameWin.setWindowTitle("Novo nome")
        self.nameWin.setStyleSheet("background-color: gray;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.nameWin.setSizePolicy(sizePolicy)
        self.nameWin.setMinimumSize(QtCore.QSize(250, 140))
        self.nameWin.setMaximumSize(QtCore.QSize(250, 140))
        self.newName = QtWidgets.QLineEdit(self.nameWin)
        self.newName.setGeometry(QtCore.QRect(30, 30, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.newName.setFont(font)
        self.newName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 115));\n"
        "color: rgb(135, 97, 88);")
        self.sendName = QtWidgets.QPushButton(self.nameWin)
        self.sendName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendName.setMaximumSize(QtCore.QSize(80, 40))
        self.sendName.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.sendName.setText("Aceitar")
        self.sendName.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0));\n")
        self.cancelName = QtWidgets.QPushButton(self.nameWin)
        self.cancelName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelName.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.cancelName.setText("Cancelar")
        self.cancelName.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0));\n")
        self.sendName.clicked.connect(self.changeName)
        self.cancelName.clicked.connect(self.nameWin.close)
        self.nameWin.show()

    def changeName(self):
        '''Envia o novo nome para o servidor'''
        name = self.newName.text()
        if name:
            self.client.sendMsg(name, CHANGE_NAME)
            self.nameWin.close()

    def sobreWin(self):
        '''Abre uma janela para selecionar e enviar arquivos'''
        file_path, _ = QFileDialog.getOpenFileName(self, "Enviar Arquivo", "", "Todos os arquivos (*.*);;Imagens (*.png *.jpg *.jpeg);;Documentos (*.pdf *.doc *.docx)")
        if file_path:
            self.send_file(file_path)

    def send_file(self, file_path):
        '''Envia um arquivo para o servidor'''
        with open(file_path, "rb") as file:
            file_data = file.read()

        file_name = os.path.basename(file_path)
        message = (f"<p><i>***{self.client} enviou um arquivo com nome {file_name}***</i></p>")
        self.client.sendMsg(message, NEW_MESSAGE)
    def get_timestamp(self):
        '''Retorna a data e hora atuais no formato dd/mm/aaaa - hh:mm:ss'''
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y - %H:%M:%S")


    def chatUpdate(self, str):
        '''Atualiza o chat com a mensagem recebida do servidor'''
        self.chat.append(str)

    def listUpdate(self, str):
        '''Atualiza a lista de usuários conectados'''
        if str == '':
            self.userList.clear()
        else:
            self.userList.append(str)

    def keyPressEvent(self, event):
        '''Envia a mensagem ao pressionar a tecla Enter'''
        key = event.key()
        if key == QtCore.Qt.Key_Return:
            self.sendBtn.click()

    def closeEvent(self, event):
        '''Encerra a conexão com o servidor ao fechar a janela'''
        if self.client.online:
            self.client.disconnect()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow("User", ADDR, PORT)

    win.show()
    app.exec_()
