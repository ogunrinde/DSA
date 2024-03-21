class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

class buildProductTree():
    def build_tree(self):
        root = TreeNode("Electronic")

        laptop = TreeNode("Laptop")
        laptop.add_child( TreeNode("Mac"))
        laptop.add_child( TreeNode("Surface"))
        laptop.add_child( TreeNode("Thinkpad"))


        phone = TreeNode("Cell Phone")
        phone.add_child( TreeNode("iPhone"))
        phone.add_child( TreeNode("Google Pixel"))
        phone.add_child( TreeNode("Vivo"))


        tv = TreeNode("TV")
        tv.add_child( TreeNode("Samsung"))
        tv.add_child( TreeNode("LG"))

        root.add_child(laptop)
        root.add_child(phone)
        root.add_child(tv)

        root.print_tree()

if __name__ == "__main__":
    bp = buildProductTree()
    bp.build_tree()

