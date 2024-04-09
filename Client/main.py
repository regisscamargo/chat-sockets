from windowLog import createWindowLog
from window import MainWindow
import sys
from PyQt5.QtWidgets import QApplication


def start():
    name, addr, port = createWindowLog()

    if name and addr and port:
        app = QApplication(sys.argv)
        win = MainWindow(name, addr, port)
        
        win.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    start()
