import sys
import os.path

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5 import QtGui
from configparser import ConfigParser

import ConfigCreate

parser = ConfigParser()
cfgfile = "config.ini"

if not os.path.exists(cfgfile):
    ConfigCreate.cfgWrite()
else:
    parser.read(cfgfile)

x_init = parser.getint('main', 'x_init')
y_init = parser.getint('main', 'y_init')
width = parser.getint('main', 'width')
height = parser.getint('main', 'height')


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initui()

    def savepos(self):
        act_width = str(self.width())
        act_height = str(self.height())
        act_x_init = str(self.pos().x())
        act_y_init = str(self.pos().y())
        parser.read(cfgfile)
        parser.set('main', 'width', act_width)
        parser.set('main', 'height', act_height)
        parser.set('main', 'x_init', act_x_init)
        parser.set('main', 'y_init', act_y_init)
        file = open(cfgfile, 'w')
        parser.write(file, space_around_delimiters=False)
        file.close()

    def initui(self):
        # Definiowanie akcji paska menu
        exitAction = QAction(QIcon('images/exit.png'), '&Wyjście', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Zamknij program')
        exitAction.triggered.connect(qApp.quit)

        savePosition = QAction(QIcon('images/diskette2.png'), 'Zapisz ustawienia okna', self)
        savePosition.setStatusTip('Zapisuje rozmiar oraz pozycję okna na pulpicie')
        savePosition.triggered.connect(self.savepos)

        # Konstruowanie paska menu
        menubar = self.menuBar()
        filemenu = menubar.addMenu('Pli&k')
        filemenu.addAction(exitAction)
        commenu = menubar.addMenu('Po&lecenia')
        viewmenu = menubar.addMenu('Wid&ok')
        cfgmenu = menubar.addMenu('&Ustawienia')
        cfgmenu.addAction(savePosition)

        # Konstrukcja paska narzędziowego
        tb1 = self.addToolBar("Pasek 1")
        new = QAction(QIcon("images/newfile.png"), "Nowy plik", self)
        tb1.setIconSize(QtCore.QSize(32, 32))
        tb1.setMovable(False)
        tb1.addAction(new)
        self.addToolBarBreak()

        tb2 = self.addToolBar("Pasek 2")
        tb2.setIconSize(QtCore.QSize(16, 16))
        tb2.setMovable(False)
        tb2.addAction(new)

        self.setGeometry(x_init, y_init, width, height)
        self.setWindowTitle('Moje Pliki')
        self.setStyleSheet("background-color: lightgray;")
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.statusBar()
        self.show()


def main():
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
