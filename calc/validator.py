import typing

from PyQt5.QtGui import QValidator


class CalculatorValidator(QValidator):
    def __init__(self, parent=None):
        super(CalculatorValidator, self).__init__(parent)
        self.allowed_characters = ['+', '-', '/', '.', '*', '^', '(', ')', '1',
                                   '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def validate(self, text_input: str, pos: int) -> typing.Tuple['QValidator.State', str, int]:
        if not text_input:
            return QValidator.Acceptable, text_input, pos
        for ch in text_input:
            if ch in self.allowed_characters:
                return QValidator.Acceptable, text_input, pos
        return QValidator.Invalid, text_input, pos
