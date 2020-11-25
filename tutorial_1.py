from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("Tutorial 1")
        self.init_ui()

    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello")
        self.label.move(50, 50)

        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setText("Click Here!")
        self.button_1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Its been clicked!")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
