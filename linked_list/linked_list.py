class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ ' -> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_the_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr.next:
            count = count + 1
            itr = itr.next
        return count
    
    def insert_at(self, data, index):
        if self.head is None:
            self.insert_at_the_beginning(data)
            return 
        
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        itr = self.head
        count = 0
        while itr:
            if index - 1 == count:
               itr.next = Node( data, itr.next )
               break
            itr = itr.next
            count = count + 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        itr = self.head
        count = 0
        while itr:
            if index - 1 == count:
                itr.next = itr.next.next
            itr = itr.next
            count = count + 1

    def insert_after_value(self, value, data):
        if self.head is None:
            self.head = Node(data, None)
            return 

        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next

    def remove_after_value(self, value):
        if self.head is None:
            return

        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_the_beginning(23)
    ll.insert_at_the_beginning(63)
    ll.insert_at_the_beginning(3)
    ll.insert_at_the_beginning(56)
    ll.insert_at_the_end(90)
    ll.insert_at(99,1)
    ll.insert_at(15,4)
    ll.insert_after_value(15, 44)
    ll.insert_after_value(90, 144)
    ll.remove_after_value(63)
    #ll.remove_at(2)

    ll.print()