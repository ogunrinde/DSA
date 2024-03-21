from collections import deque
class BinaryNumberWithQueue:
    def __init__(self):
        self.binary_number = deque()

    def enqueue(self):
        num = 1
        i = 1
        while i < 10:
            self.binary_number.appendleft(num)