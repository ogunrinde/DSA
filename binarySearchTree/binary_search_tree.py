class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def add_child(self, data):
        if self.data == data:
            return 

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.data == None:
            return None

        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.data == None:
            return None

        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        cal_sum = 0

        if self.left:
            cal_sum = cal_sum + self.left.calculate_sum()

        cal_sum = cal_sum + self.data
    
        if self.right:
            cal_sum = cal_sum + self.right.calculate_sum()

        return cal_sum

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements


class BuildTree():
    def build_tree(self, elements):
        print("Building tree with these elements:",elements)
        root = BinarySearchTreeNode(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])

        return root


if __name__ == "__main__":
    bt = BuildTree()
    numbers_tree = bt.build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Is 17 present:", numbers_tree.search(17))
    print("Is 34 present:", numbers_tree.search(34))
    print("Is 20 present:", numbers_tree.search(201))
    print("Find the minimum value:", numbers_tree.find_min())
    print("Find the maximum value:", numbers_tree.find_max())
    print("Find the Sum:", numbers_tree.calculate_sum())
    print("Post Order traversal gives this sorted list:",numbers_tree.post_order_traversal())


