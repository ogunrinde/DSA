class LoadData():
    def load(self):
        stock_prices = {}
        with open("stock_prices.csv","r") as f:
            for line in f:
                row = line.split(',')
                day = row[0]
                price = row[1]
                stock_prices[day] = price
        return stock_prices

    def getPrice(self, key, stock_prices):
        return stock_prices[key]


class Hash():
    def __init__(self):
        self.MAX = 100
        self.arr = [ None for i in range(self.MAX) ]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        print( hash % self.MAX)
        return hash % self.MAX

    def __getitem__(self, index):
        key = self.get_hash(index)
        return self.arr[key]

    def __setitem__(self, index, val):
        key = self.get_hash(index)
        self.arr[key] = val

    def __delitem__(self, index):
        key = self.get_hash(index)
        self.arr[key] = None


if __name__ == "__main__":
    t = Hash()
    # stock_prices = ld.load()
    # price = ld.getPrice('march 6', stock_prices)
    # ld.get_hash('march 7')
    t['march 10'] = 310
    t.get_hash('march 6')
    t.get_hash('march 17')
