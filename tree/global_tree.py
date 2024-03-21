class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
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

    def print_tree_by_level(self, level):
        if level + 1 <= self.get_level():
            return 
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree_by_level(level)
    
class BuildGlobalTree:
    def build_global_tree(self):
        root = TreeNode("Global")

        india = TreeNode("India")

        gu = TreeNode("Gujarat")
        gu.add_child(TreeNode("Ahmedabad"))
        gu.add_child(TreeNode("Baroda"))

        ka = TreeNode("Karnataka")
        ka.add_child(TreeNode("Bangluru"))
        ka.add_child(TreeNode("Mysore"))

        india.add_child(gu)
        india.add_child(ka)


        usa = TreeNode("USA")

        nj = TreeNode("New Jersey")
        nj.add_child(TreeNode("Princeton"))
        nj.add_child(TreeNode("Trenton"))
        
        ca = TreeNode("California")
        ca.add_child(TreeNode("San Francisco"))
        ca.add_child(TreeNode("Mountain View"))
        ca.add_child(TreeNode("Palo Alto"))

        usa.add_child(nj)
        usa.add_child(ca)

        root.add_child(india)
        root.add_child(usa)

        #root.print_tree()
        root.print_tree_by_level(3)


if __name__ == "__main__":
    bgt = BuildGlobalTree()
    bgt.build_global_tree()

