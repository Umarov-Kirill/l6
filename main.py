import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: black")

        self.hbox_line = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox_res = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.vbox.addLayout(self.hbox_line)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox_res)

        self.line = QLineEdit(self)
        self.line.setEnabled(False)
        self.line.setStyleSheet("background-color: green")
        self.button1 = QPushButton("1", self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.buttonadd = QPushButton("+", self)
        self.buttonres = QPushButton("=", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.buttonsub = QPushButton("-", self)
        self.buttonmult = QPushButton("*", self)
        self.button7 = QPushButton("7", self)
        self.button8 = QPushButton("8", self)
        self.button9 = QPushButton("9", self)
        self.button0 = QPushButton("0", self)
        self.buttondiv = QPushButton("/", self)
        self.buttonclear = QPushButton("C", self)
        self.buttondot = QPushButton(".", self)
        self.buttonbackspace = QPushButton("BS", self)
        self.button1.setStyleSheet("background-color: green")
        self.button2.setStyleSheet("background-color: green")
        self.button3.setStyleSheet("background-color: green")
        self.button4.setStyleSheet("background-color: green")
        self.button5.setStyleSheet("background-color: green")
        self.button6.setStyleSheet("background-color: green")
        self.button7.setStyleSheet("background-color: green")
        self.button8.setStyleSheet("background-color: green")
        self.button9.setStyleSheet("background-color: green")
        self.buttonadd.setStyleSheet("background-color: green")
        self.buttonres.setStyleSheet("background-color: green")
        self.buttonsub.setStyleSheet("background-color: green")
        self.buttonmult.setStyleSheet("background-color: green")
        self.buttondiv.setStyleSheet("background-color: green")
        self.buttonclear.setStyleSheet("background-color: green")
        self.buttondot.setStyleSheet("background-color: green")
        self.buttonbackspace.setStyleSheet("background-color: green")
        self.button0.setStyleSheet("background-color: green")
        self.hbox_line.addWidget(self.line)
        self.hbox1.addWidget(self.buttonadd)
        self.hbox1.addWidget(self.buttonsub)
        self.hbox1.addWidget(self.buttonres)
        self.hbox1.addWidget(self.button1)
        self.hbox1.addWidget(self.button2)
        self.hbox1.addWidget(self.button3)
        self.hbox2.addWidget(self.buttonmult)
        self.hbox2.addWidget(self.buttondiv)
        self.hbox2.addWidget(self.buttonclear)
        self.hbox2.addWidget(self.button4)
        self.hbox2.addWidget(self.button5)
        self.hbox2.addWidget(self.button6)
        self.hbox3.addWidget(self.buttonbackspace)
        self.hbox3.addWidget(self.buttondot)
        self.hbox3.addWidget(self.button0)
        self.hbox3.addWidget(self.button7)
        self.hbox3.addWidget(self.button8)
        self.hbox3.addWidget(self.button9)

        self.setLayout(self.vbox)

        self.button1.clicked.connect(lambda: self.addText("1"))
        self.button2.clicked.connect(lambda: self.addText("2"))
        self.button3.clicked.connect(lambda: self.addText("3"))
        self.buttonadd.clicked.connect(lambda: self.operation("+"))
        self.buttonres.clicked.connect(self.result)
        self.button4.clicked.connect(lambda: self.addText("4"))
        self.button5.clicked.connect(lambda: self.addText("5"))
        self.button6.clicked.connect(lambda: self.addText("6"))
        self.buttonsub.clicked.connect(lambda: self.operation("-"))
        self.buttonmult.clicked.connect(lambda: self.operation("*"))
        self.button7.clicked.connect(lambda: self.addText("7"))
        self.button8.clicked.connect(lambda: self.addText("8"))
        self.button9.clicked.connect(lambda: self.addText("9"))
        self.button0.clicked.connect(lambda: self.addText("0"))
        self.buttondiv.clicked.connect(lambda: self.operation("/"))
        self.buttonclear.clicked.connect(lambda: self.clearText())
        self.buttondot.clicked.connect(lambda: self.addText("."))
        self.buttonbackspace.clicked.connect(lambda: self.backspace())

    def addText(self, param):
        line = self.line.text()
        self.line.setText(line + param)

    def operation(self, param):
        self.check = self.line.text()
        if self.check:
            self.num1 = self.line.text()
            self.line.setText("")
            self.op = param
        else:
            pass
    def result(self):
        self.num2 = self.line.text()
        try:
            self.num1
        except AttributeError:
            return
        try:
            float(self.num1)
            float(self.num2)
        except ValueError:
            return
        if self.op == "+":
            self.line.setText(str(float(self.num1) + float(self.num2)))
        if self.op == "-":
            self.line.setText(str(float(self.num1) - float(self.num2)))
        if self.op == "*":
            self.line.setText(str(float(self.num1) * float(self.num2)))
        if self.op == "/":
            try:
                self.line.setText(str(float(self.num1)/float(self.num2)))
            except ZeroDivisionError:
                self.line.setText("Error")
        else:
            pass

    def clearText(self):
        self.line.setText("")

    def backspace(self):
        self.edit = self.line.text()
        if self.edit:
            try:
                float(self.edit)
            except ValueError:
                self.line.setText("Error")
                return
            self.edit = list(self.edit)
            self.edit.pop()
            self.edit=''.join(self.edit)
            self.line.setText(self.edit)
        else:
            pass

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Plus:
            self.operation("+")
        if e.key() == Qt.Key_Minus:
            self.operation("-")
        if e.key() == Qt.Key_Enter:
            self.result()
        if e.key() == Qt.Key_Equal:
            self.result()
        if e.key() == Qt.Key_Slash:
            self.operation("/")
        if e.key() == Qt.Key_Asterisk:
            self.operation("*")
        if e.key() == Qt.Key_1:
            self.addText("1")
        if e.key() == Qt.Key_2:
            self.addText("2")
        if e.key() == Qt.Key_3:
            self.addText("3")
        if e.key() == Qt.Key_4:
            self.addText("4")
        if e.key() == Qt.Key_5:
            self.addText("5")
        if e.key() == Qt.Key_6:
            self.addText("6")
        if e.key() == Qt.Key_7:
            self.addText("7")
        if e.key() == Qt.Key_8:
            self.addText("8")
        if e.key() == Qt.Key_9:
            self.addText("9")
        if e.key() == Qt.Key_0:
            self.addText("0")
        if e.key() == Qt.Key_Period:
            self.addText(".")
        if e.key() == Qt.Key_Delete:
            self.clearText()
        if e.key() == Qt.Key_Backspace:
            self.backspace()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Calculator")

    win = Window()
    win.show()
    sys.exit(app.exec_())
