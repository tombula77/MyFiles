import sys
import os.path

from PyQt5.QtWidgets import *

from configparser import ConfigParser

import ConfigCreate

config = ConfigParser()
cfgfile = "config.ini"

if not os.path.exists(cfgfile):
    ConfigCreate.cfgWrite()
else:
    config.read(cfgfile)

x_init = config.getint('main', 'x_init')
y_init = config.getint('main', 'y_init')
width = config.getint('main', 'width')
height = config.getint('main', 'height')


def empty():
    pass


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(x_init, y_init, width, height)
        self.setWindowTitle('MyFiles')
        self.setStyleSheet("background-color: lightgray;")


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    sys.exit(app.exec_())
