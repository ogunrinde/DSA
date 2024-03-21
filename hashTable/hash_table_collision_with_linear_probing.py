class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [ None for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        index = self.get_hash(key)
        if self.arr[index] is None:
            return 
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
    
    def __setitem__(self, key, val):
        index = self.get_hash(key)
        if self.arr[index] is None:
            self.arr[index] = (key, val)
        else:
            pos = self.find_slot(key, val)
            self.arr[pos] = (key, val)
        print(self.arr)

    def get_prob_range(self,index):
        return [ *range(index, len(self.arr)) ] + [ *range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

if __name__ == "__main__":
    t = HashTable()
    t['march 6'] = 20
    t['march 17'] = 20