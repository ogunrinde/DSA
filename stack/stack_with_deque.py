from collections import deque
class StackWithDeque():
    def __init__(self):
        self.stack = deque()

    def append(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def print(self):
        print(self.stack)


if __name__ == "__main__":
    s = StackWithDeque()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(5)
    s.pop()
    s.print()
