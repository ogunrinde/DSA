class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)


    def printforward(self):
        if self.head is None:
            print("Linked list is empty")
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data)+' -> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def printbackward(self):
        if self.head is None:
            print("Linked lis is empty")
        itr = self.head
        while itr.next:
            itr = itr.next
        llstr = ""
        while itr.prev:
            llstr += str(itr.data)+ '-> ' if itr.prev else itr.data
            itr = itr.prev
        print(llstr)
    

if __name__ == "__main__":
    ll = DoubleLinkedList()
    ll.insert_at_beginning(13)
    ll.insert_at_beginning(45)
    ll.insert_at_beginning(62)
    ll.insert_at_beginning(10)
    ll.insert_at_end(16)
    ll.insert_at_end(96)
    ll.printforward()
    ll.printbackward()
