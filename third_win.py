from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from options import *
from second_win import *

def HeartWork():
    if (age == 7 or age == 8) and index >= 21:
        heart = 'low'
    elif (age == 7 or age == 8) and (index > 17 and index < 20.9):
        heart = 'satisfactory'
    elif (age == 7 or age == 8) and (index > 12 and index < 16.9):
        heart = 'medium'
    elif (age == 7 or age == 8) and (index > 6.5 and index < 11.9):
        heart = 'above average'
    elif (age == 7 or age == 8) and index <= 6.4:
        heart = 'high'
    if (age == 9 or age == 10) and index >= 19.5:
        heart = 'low'
    elif (age == 9 or age == 10) and (index > 15.5 and index < 19.4):
        heart = 'satisfactory'
    elif (age == 9 or age == 10) and (index > 10.5 and index < 15.4):
        heart = 'medium'
    elif (age == 9 or age == 10) and (index > 5 and index < 10.4):
        heart = 'above average'
    elif (age == 9 or age == 10) and index <= 4.9:
        heart = 'high'
    if (age == 11 or age == 12) and index >= 18:
        heart = 'low'
    elif (age == 11 or age == 12) and (index > 14 and index < 17.9):
        heart = 'satisfactory'
    elif (age == 11 or age == 12) and (index > 9 and index < 13.9):
        heart = 'medium'
    elif (age == 11 or age == 12) and (index > 3.5 and index < 8.9):
        heart = 'above average'
    elif (age == 11 or age == 12) and index <= 3.4:
        heart = 'high'
    if (age == 13 or age == 14) and index >= 16.5:
        heart = 'low'
    elif (age == 13 or age == 14) and (index > 12.5 and index < 16.4):
        heart = 'satisfactory'
    elif (age == 13 or age == 14) and (index > 7.5 and index < 12.4):
        heart = 'medium'
    elif (age == 13 or age == 14) and (index > 2 and index < 7.4):
        heart = 'above average'
    elif (age == 13 or age == 14) and index <= 1.9:
        heart = 'high'
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        
        self.show()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(win_title)
        self.setWindowIcon(QtGui.QIcon(pulse_icon))

    def initUI(self):
        self.rufieindex = QLabel(rufieindex, index)
        self.heart_work = QLabel(heart_work)

        self.vline = QVBoxLayout()
        self.vline.addWidget(self.rufieindex, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.vline.addWidget(self.heart_work, alignment=Qt.AlignCenter)
        self.setLayout(self.vline)

app = QApplication([])
win = FinalWin()
app.exec_()
