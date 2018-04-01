import sys
from PyQt5 import QtWidgets
import tscript76

class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        box = QtWidgets.QVBoxLayout(self)
        self.input = QtWidgets.QLineEdit()
        self.result = QtWidgets.QLabel()
        self.enter = QtWidgets.QPushButton()
        self.enter.clicked.connect(self.show_result)
        box.addWidget(self.input)
        box.addWidget(self.result)
        box.addWidget(self.enter)

    def show_result(self):
        self.result.setNum(tscript76.func_sum(self.input.text()))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
