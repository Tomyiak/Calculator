import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLineEdit, QHBoxLayout,
                             QVBoxLayout, QPushButton)


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        # General VBoxLayout
        self.vbox = QVBoxLayout(self)

        # HBoxLayout
        self.hbox_result = QHBoxLayout()  # Создаём 5 строку
        self.hbox_input = QHBoxLayout()  # Создаём строку ввода
        self.hbox_first = QHBoxLayout()  # Создаём 1 строку
        self.hbox_second = QHBoxLayout()  # Создаём 2 строку
        self.hbox_third = QHBoxLayout()  # Создаём 3 строку
        self.hbox_fourth = QHBoxLayout()  # Создаём 4 строку

        # Connect hbox and Layout
        self.vbox.addLayout(self.hbox_input)  # Добавляем строку вывода
        self.vbox.addLayout(self.hbox_first)  # Добавляем 1 строку
        self.vbox.addLayout(self.hbox_second)  # Добавляем 2 строку
        self.vbox.addLayout(self.hbox_third)  # Добавляем 3 строку
        self.vbox.addLayout(self.hbox_fourth)  # Добавляем 4 строку
        self.vbox.addLayout(self.hbox_result)  # Добавляем 5 строку

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # Button "1"
        self.b_1 = QPushButton("1", self)
        self.hbox_second.addWidget(self.b_1)

        # Button "2"
        self.b_2 = QPushButton("2", self)
        self.hbox_second.addWidget(self.b_2)

        # Button "3"
        self.b_3 = QPushButton("3", self)
        self.hbox_second.addWidget(self.b_3)

        # Button "4"
        self.b_4 = QPushButton("4", self)
        self.hbox_third.addWidget(self.b_4)

        # Button "5"
        self.b_5 = QPushButton("5", self)
        self.hbox_third.addWidget(self.b_5)

        # Button "6"
        self.b_6 = QPushButton("6", self)
        self.hbox_third.addWidget(self.b_6)

        # Button "7"
        self.b_7 = QPushButton("7", self)
        self.hbox_fourth.addWidget(self.b_7)

        # Button "8"
        self.b_8 = QPushButton("8", self)
        self.hbox_fourth.addWidget(self.b_8)

        # Button "9"
        self.b_9 = QPushButton("9", self)
        self.hbox_fourth.addWidget(self.b_9)

        # Button "/"
        self.b_division = QPushButton("/", self)
        self.hbox_result.addWidget(self.b_division)

        # Button "0"
        self.b_0 = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_0)

        # Button "+"
        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        # Button "-"
        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)

        # Button "*"
        self.b_multiplication = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiplication)

        # Button "="
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        # Button "."
        self.b_dot = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_dot)

        # Регистрация нажатия кнопок операций
        self.b_plus.clicked.connect(lambda: self.operation("+"))
        self.b_minus.clicked.connect(lambda: self.operation("-"))
        self.b_multiplication.clicked.connect(lambda: self.operation("*"))
        self.b_division.clicked.connect(lambda: self.operation("/"))
        self.b_result.clicked.connect(self._result)

        # Регистрация нажатия кнопок чисел
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_dot.clicked.connect(lambda: self._button("."))


        self.move(350, 300)
        self.setWindowTitle('Calculator')
        self.show()

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def operation(self, op):
        self.num_1 = float(self.input.text())
        self.op = op
        self.input.setText("")

    def _result(self):
        self.num_2 = float(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "/":
            if self.num_2 == 0:
                self.input.setText("ZeroDivisionError: division by zero")
            else:
                self.input.setText(str(self.num_1 / self.num_2))
        elif self.op == "=":
            pass
        if self.num_2 == "" and self.num_2 == " ":
            self.input.setText("Error")


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())