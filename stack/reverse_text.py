from collections import deque
class ReverseText():
    def __init__(self):
        self.stack = deque()
        self.string = "We will conquere COVID-19"

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def append(self):
        for char in self.string:
            self.stack.append(char)
        print(self.stack)

    def pop(self):
        self.string = ""
        for i in range(len(self.stack)):
            self.string += self.stack.pop()

        print(self.string)
        return self.string

    
if __name__ == "__main__":
    r = ReverseText()
    r.append()
    r.pop()