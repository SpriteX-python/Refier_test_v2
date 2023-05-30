from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from options import *


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(win_title)
        self.setWindowIcon(QtGui.QIcon(pulse_icon))

    def initUI(self):
        pass

    def connects(self):
        pass

    def next_win(self):
        pass


app = QApplication([])
win = SecondWin()
app.exec_()
