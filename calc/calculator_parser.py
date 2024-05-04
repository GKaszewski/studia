from typing import List, Dict


class ShuntingYardAlgorithm:
    def __init__(self):
        self.queue: List[str] = []
        self.op_stack: List[str] = []
        self.op_precedence: Dict[str, int] = {'P': 1, 'E': 2, 'M': 3, 'A': 4}
        self.op_characters: List[str] = ['+', '-', '*', '/', '^', '(', ')']
        self.num_characters: List[str] = ['1', '2', '3', '4', '5', '6', '7',
                                          '8', '9', '0']

    def reset_containers(self) -> None:
        self.queue = []
        self.op_stack = []

    def convert_op_to_pemdas(self, op: str) -> str:
        if op in ['(', ')']:
            return 'P'
        elif op == '^':
            return 'E'
        elif op in ['*', '/']:
            return 'M'
        elif op in ['+', '-']:
            return 'A'

    def convert_to_rpn(self, text: str) -> List[str]:
        self.reset_containers()
        for ch in text:
            if ch in self.op_characters:
                if self.op_stack:
                    if self.convert_op_to_pemdas(self.op_stack[-1]) != 'P':
                        last_op = self.op_stack[-1]
                        last_op_precedence = self.op_precedence[
                            self.convert_op_to_pemdas(last_op)]
                        current_op_precedence = self.op_precedence[
                            self.convert_op_to_pemdas(ch)]
                        if last_op_precedence < current_op_precedence:
                            self.op_stack.pop()
                            self.queue.append(last_op)
                            self.op_stack.append(ch)
                        else:
                            self.op_stack.append(ch)
                    else:
                        self.op_stack.append(ch)
                    if ch == ')':
                        while self.op_stack:
                            current_op = self.op_stack.pop()
                            if current_op == '(' or current_op == ')':
                                continue

                            self.queue.append(current_op)
                else:
                    self.op_stack.append(ch)
            elif ch in self.num_characters:
                self.queue.append(ch)
        while self.op_stack:
            self.queue.append(self.op_stack.pop())
        return self.queue


class PostfixStackEvaluator:
    pass