from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from options import *


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
        self.setWindowIcon(QtGui.QIcon('pulse.png'))

    def initUI(self):
        self.hello = QLabel('Welcome to the health assessment program!')
        self.txt_instruction = QLabel('This application will allow you to use the Rufier test to conduct a primary '
                                      'diagnosis of your health.\n'
                                      'The Rufier test is a load complex designed to assess performance '
                                      'hearts during physical exertion.\n'
                                      'The pulse rate is determined in the subject who is lying on his back for 5 '
                                      'minutes in 15 seconds;\n'
                                      'then, within 45 seconds, the subject performs 30 squats.\n'
                                      'After the end of the load, the subject lies down, and the number of pulsations '
                                      'for him is counted again.'
                                      'the first 15 seconds,\n'
                                      'and then — for the last 15 seconds of the first minute of the recovery period.\n'
                                      'Important! If you feel unwell during the test\n'
                                      '(dizziness will appear, tinnitus, severe shortness of breath, etc.)\n'
                                      'then the test should be interrupted and consult a doctor.')
        self.vline = QVBoxLayout()
        self.vline.addWidget(self.hello, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(self.vline)

    def connects(self):
        pass


app = QApplication([])
win = MainWin()
app.exec_()
