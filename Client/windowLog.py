import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from config import *


def createWindowLog():
    app = QApplication(sys.argv)
    win = LogWindow()
    win.show()
    app.exec_()
    return (win.name, win.addr, win.prt)


class LogWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi()
        self.name = False
        self.addr = False
        self.prt = False

    def setupUi(self):
        self.setWindowIcon(QIcon("img\\miniLogo.png"))
        self.setObjectName("LogWindow")
        self.resize(470, 602)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.971591 rgba(255, 255, 255, 255));")

        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        font1 = QFont()
        font1.setPointSize(14)
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(12)
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(18)
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setWeight(75)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy1)
        self.logo.setMaximumSize(QSize(200, 200))
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setAutoFillBackground(False)
        self.logo.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Plain)
        self.logo.setPixmap(QPixmap(u"img\\logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));")
        self.gridLayout.addWidget(self.logo, 1, 1, 1, 1, Qt.AlignHCenter)

        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMaximumSize(QSize(16777215, 40))
        self.titulo.setFont(font4)
        self.titulo.setLayoutDirection(Qt.LeftToRight)
        self.titulo.setFrameShape(QFrame.NoFrame)
        self.titulo.setFrameShadow(QFrame.Plain)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: black;")
        self.gridLayout.addWidget(self.titulo, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: black;")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: black;")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 1)

        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setMaximumSize(QSize(400, 31))
        self.username.setFont(font2)
        self.username.setFocus()
        self.username.setStyleSheet(u"background-color: white;")
        self.gridLayout.addWidget(self.username, 6, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: black;")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)

        self.adress = QLineEdit(self.centralwidget)
        self.adress.setObjectName(u"adress")
        self.adress.setMaximumSize(QSize(400, 31))
        self.adress.setFont(font2)
        self.adress.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.adress, 9, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: black;")
        self.gridLayout.addWidget(self.label_4, 10, 1, 1, 1)

        self.port = QLineEdit(self.centralwidget)
        self.port.setObjectName(u"port")
        self.port.setMaximumSize(QSize(400, 31))
        self.port.setFont(font2)
        self.port.setStyleSheet(u"background-color: white")
        self.gridLayout.addWidget(self.port, 11, 1, 1, 1)

        self.error = QLabel(self)
        self.error.setObjectName(u"errorLabel")
        self.error.setFont(font)
        self.error.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n color: red;")
        self.gridLayout.addWidget(self.error, 12, 1, 1, 1)

        self.entrar = QPushButton(self.centralwidget)
        self.entrar.setObjectName(u"entrar")
        self.entrar.setSizeIncrement(QSize(0, 0))
        self.entrar.setBaseSize(QSize(0, 0))
        self.entrar.setFont(font1)
        self.entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.entrar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 0));\n color: blue;")
        self.gridLayout.addWidget(self.entrar, 13, 1, 1, 1)
        self.entrar.clicked.connect(self.login)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 14, 1, 1, 1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.setCentralWidget(self.centralwidget)

        self.completeUi()
        QMetaObject.connectSlotsByName(self)

    def completeUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"Chat dos Gurizes", None))
        self.label_4.setText(QCoreApplication.translate("self", u"Porta", None))
        self.label_3.setText(QCoreApplication.translate("self", u"Endereco de IP", None))
        self.entrar.setText(QCoreApplication.translate("self", u"Entrar", None))
        self.label_5.setText(QCoreApplication.translate("self", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("self", u"Username", None))
        self.titulo.setText(QCoreApplication.translate("self", u"Chat dos Gurizes", None))
        self.logo.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("self", u"Lulu dos Codigo Perigoso", None))
        self.adress.setPlaceholderText(QCoreApplication.translate("self", u"123.456.1.890", None))
        self.port.setPlaceholderText(QCoreApplication.translate("self", u"5000", None))

    def login(self):
        self.name = self.username.text()
        self.addr = str(self.adress.text())
        self.prt = self.port.text()
        if len(self.name) == 0:
            self.name = 'Luciano dos Codigo Perigoso'
        if len(self.addr) == 0:
            self.addr = SERVER
        if len(self.prt) == 0:
            self.prt = PORT
        self.close()

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Return:
            self.login()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LogWindow()
    win.show()
    app.exec_()
