class StackWithList():
    def __init__(self):
        self.list = []

    def append(self, item):
        self.list.append(item)
    
    def pop(self):
        self.list.pop()

    def print(self):
        print(self.list)


if __name__ == '__main__':
    s = StackWithList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    s.print()