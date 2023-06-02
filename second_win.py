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
        self.hello = QLabel(hello)

        self.vline = QVBoxLayout()
        self.vline.addWidget(self.hello, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(self.vline)

    def connects(self):
        pass

    def next_win(self):
        pass
    #SDGASGHASRFGHASRH


app = QApplication([])
win = SecondWin()
app.exec_()
