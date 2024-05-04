from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, left=None, right=None, value=None, func=None):
        self.left: Node[T] = left
        self.right: Node[T] = right
        self.value: T = value
        self.evaluate = func


def solve(node: Node) -> T:
    if node.value:
        return node.value
    if not node.left.value:
        node.left.value = solve(node.left)
    if not node.right.value:
        node.right.value = solve(node.right)
    node.value = node.evaluate(node.left.value, node.right.value)
    return node.value
