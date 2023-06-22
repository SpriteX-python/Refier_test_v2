# from PyQt5 import QtGui
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import *
# from options import *
#
#
# def HeartWork(index):
#     if (age == 7 or age == 8) and index >= 21:
#         heart = 'low'
#     elif (age == 7 or age == 8) and (index > 17 and index < 20.9):
#         heart = 'satisfactory'
#     elif (age == 7 or age == 8) and (index > 12 and index < 16.9):
#         heart = 'medium'
#     elif (age == 7 or age == 8) and (index > 6.5 and index < 11.9):
#         heart = 'above average'
#     elif (age == 7 or age == 8) and index <= 6.4:
#         heart = 'high'
#     if (age == 9 or age == 10) and index >= 19.5:
#         heart = 'low'
#     elif (age == 9 or age == 10) and (index > 15.5 and index < 19.4):
#         heart = 'satisfactory'
#     elif (age == 9 or age == 10) and (index > 10.5 and index < 15.4):
#         heart = 'medium'
#     elif (age == 9 or age == 10) and (index > 5 and index < 10.4):
#         heart = 'above average'
#     elif (age == 9 or age == 10) and index <= 4.9:
#         heart = 'high'
#     if (age == 11 or age == 12) and index >= 18:
#         heart = 'low'
#     elif (age == 11 or age == 12) and (index > 14 and index < 17.9):
#         heart = 'satisfactory'
#     elif (age == 11 or age == 12) and (index > 9 and index < 13.9):
#         heart = 'medium'
#     elif (age == 11 or age == 12) and (index > 3.5 and index < 8.9):
#         heart = 'above average'
#     elif (age == 11 or age == 12) and index <= 3.4:
#         heart = 'high'
#     if (age == 13 or age == 14) and index >= 16.5:
#         heart = 'low'
#     elif (age == 13 or age == 14) and (index > 12.5 and index < 16.4):
#         heart = 'satisfactory'
#     elif (age == 13 or age == 14) and (index > 7.5 and index < 12.4):
#         heart = 'medium'
#     elif (age == 13 or age == 14) and (index > 2 and index < 7.4):
#         heart = 'above average'
#     elif (age == 13 or age == 14) and index <= 1.9:
#         heart = 'high'
#     return heart
#
#
# class FinalWin(QWidget):
#     def __init__(self, exp):
#         super().__init__()
#         self.set_appear()
#         self.exp = exp
#         self.amount()
#         self.initUI()
#         self.show()
#
#     def amount(self):
#         self.index = (self.exp.t1 + self.exp.t2 + self.exp.t3) - 200 / 10
#
#     def set_appear(self):
#         self.resize(win_width, win_height)
#         self.setWindowTitle(win_title)
#         self.setWindowIcon(QtGui.QIcon(pulse_icon))
#
#     def initUI(self):
#         self.rufieindex = QLabel(rufieindex + self.index)
#         self.heart_work = QLabel(heart_work + HeartWork(self.index))
#
#         self.vline = QVBoxLayout()
#         self.vline.addWidget(self.rufieindex, alignment=Qt.AlignCenter | Qt.AlignTop)
#         self.vline.addWidget(self.heart_work, alignment=Qt.AlignCenter)
#         self.setLayout(self.vline)
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout, QGridLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from options import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.show()

    def results(self):
        if self.exp.age < 60:
            self.index = 0
            return "no data for this age"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5

    def initUI(self):
        ''' создаёт графические элементы '''
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(rufieindex + str(self.index))

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        # self.move(win_x, win_y)