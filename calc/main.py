import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit

from calculator_parser import ShuntingYardAlgorithm
from validator import CalculatorValidator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('calc_ui.ui', self)
        self.sign = False
        self.text_input.setValidator(CalculatorValidator())
        self.setup_buttons()
        self.show()

    def setup_buttons(self) -> None:
        self.clear_btn.clicked.connect(self.clear)
        self.delete_btn.clicked.connect(self.delete)
        self.one_btn.clicked.connect(lambda: self.put_character('1'))
        self.two_btn.clicked.connect(lambda: self.put_character('2'))
        self.three_btn.clicked.connect(lambda: self.put_character('3'))
        self.four_btn.clicked.connect(lambda: self.put_character('4'))
        self.five_btn.clicked.connect(lambda: self.put_character('5'))
        self.six_btn.clicked.connect(lambda: self.put_character('6'))
        self.seven_btn.clicked.connect(lambda: self.put_character('7'))
        self.eight_btn.clicked.connect(lambda: self.put_character('8'))
        self.nine_btn.clicked.connect(lambda: self.put_character('9'))
        self.dot_btn.clicked.connect(lambda: self.put_character('.'))
        self.add_btn.clicked.connect(lambda: self.put_character('+'))
        self.substract_btn.clicked.connect(lambda: self.put_character('-'))
        self.multiply_btn.clicked.connect(lambda: self.put_character('*'))
        self.divide_btn.clicked.connect(lambda: self.put_character('/'))
        self.sign_btn.clicked.connect(self.change_sign)
        self.calc_btn.clicked.connect(self.calculate)

    def clear(self) -> None:
        self.text_input.clear()

    def delete(self) -> None:
        self.text_input: QLineEdit
        current_text = self.text_input.text()
        self.text_input.setText(current_text[:-1])

    def put_character(self, character: str) -> None:
        self.text_input: QLineEdit
        current_text = self.text_input.text()
        self.text_input.setText(current_text + character)

    def change_sign(self) -> None:
        self.text_input: QLineEdit
        if self.sign:
            self.sign = False
            self.text_input.cursorBackward(False, 2)
            self.text_input.del_()
            self.text_input.cursorForward(False)
        else:
            self.sign = True
            self.text_input.cursorBackward(False)
            self.text_input.insert('-')
            self.text_input.cursorForward(False)

    def calculate(self) -> None:
        shunting = ShuntingYardAlgorithm()
        result = shunting.convert_to_rpn(self.text_input.text())
        print(f'Result: {result}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    # calculator = Node[int](left=Node(value=10), right=Node(value=2),
    #                        func=lambda x, y: x * y)
    # result = solve(calculator)
    # print(f'Result of {calculator.left.value}*{calculator.right.value}: {result}')
