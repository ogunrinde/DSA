class listQueue:
    def __init__(self):
        self.stock_price_queue = []

    def insert(self, val):
        self.stock_price_queue.insert(0,val)

    def print(self):
        print(self.stock_price_queue)

    def pop(self):
        self.stock_price_queue.pop()


if __name__ == "__main__":
    lq = listQueue()
    lq.insert(1)
    lq.insert(2)
    lq.insert(3)
    lq.print()
    lq.pop()
    lq.print()