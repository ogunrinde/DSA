from collections import deque
import time
import threading
class OrderingSystem():
    def __init__(self):
        self.orders = deque()

    def place_order(self, items):
        for item in items:
            self.orders.appendleft(item)
            print(self.orders)
            time.sleep(0.5)

    def serve_order(self):
        for item in range(len(self.orders)):
            self.orders.pop()
            print(self.orders)
            time.sleep(2)


if __name__ == "__main__":
    os = OrderingSystem()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=os.place_order,args=(orders,))
    t2 = threading.Thread(target=os.serve_order)
    t1.start()
    time.sleep(1)
    t2.start()

    t1.join()
    t2.join()
