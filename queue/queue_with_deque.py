from collections import deque
class queueWithDeque():
    def __init__(self):
        self.lq = deque()

    def insert(self, val):
        self.lq.appendleft(val)

    def pop(self):
        self.lq.pop()

    def print(self):
        print(self.lq)


if __name__ == '__main__':
    lq = queueWithDeque()
    lq.insert({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    lq.insert({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    lq.insert({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })
    lq.print()


    