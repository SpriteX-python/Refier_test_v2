from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from options import *
from second_win import SecondWin


class MainWin(QWidget):
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
        self.instruction = QLabel(txt_instruction)
        self.instruction.setAlignment(Qt.AlignCenter)
        self.button_next = QPushButton(button_next)

        self.vline = QVBoxLayout()
        self.vline.addWidget(self.hello, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vline.addWidget(self.instruction, alignment=Qt.AlignCenter)
        self.vline.addWidget(self.button_next, alignment=Qt.AlignCenter)
        self.setLayout(self.vline)

    def connects(self):
        self.button_next.clicked.connect(next_win)

    def next_win(self):
        self.hide()
        self.mv = SecondWin()


app = QApplication([])
win = MainWin()
app.exec_()
