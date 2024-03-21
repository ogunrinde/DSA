class TreeNode:
    def __init__(self, name, designation):
        self.name = name 
        self.designation = designation
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


    def print_tree(self, type):
        data = None
        if type == "name":
            data = self.name
        elif type == "designation":
            data = self.designation
        else:
            data = "{} ({})".format(self.name, self.designation)
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix+data)
        if self.children:
            for child in self.children:
                child.print_tree(type)
    
class BuildManagementTree():
    def build_management_tree(self, type):
        root = TreeNode("Nilupul", "CEO")

        cto = TreeNode("Chinmay", "CTO")


        inf_head = TreeNode("Vishwa", "Infrastructure Head")
        inf_head.add_child( TreeNode("Dhaval", "Cloud Manager"))
        inf_head.add_child( TreeNode("Abhijit", "App Manager"))

        app_head = TreeNode("Aamir", "Application Head")

        cto.add_child(inf_head)
        cto.add_child(app_head)


        hr_head = TreeNode("Gels", "HR Head")
        hr_head.add_child(TreeNode("Peter", "Recruitment Manager"))
        hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

        root.add_child(cto)
        root.add_child(hr_head)

        root.print_tree(type)


if __name__ == "__main__":
    bmt = BuildManagementTree()
    bmt.build_management_tree("name")
    bmt.build_management_tree("designation")
    bmt.build_management_tree("both")

