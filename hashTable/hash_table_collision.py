class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [ [] for i in range(self.MAX) ]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    def __getitem__(self, key):
        index = self.get_hash(key)
        for kv in self.arr[index]:
            if kv[0] == key:
                return kv[1]

    
    def __setitem__(self, key, val):
        index = self.get_hash(key)
        if len(self.arr[index]) == 0:
            self.arr[index].append((key,val))

        for idx, element in enumerate(self.arr[index]):
            if len(element) == 2 and element[0] == key:
                self.arr[index][idx] = (key, val)


    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, element in enumerate(self.arr[index]):
            if element[0] == key:
                del self.arr[index][idx]


if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    print(t.arr)