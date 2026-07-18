# implement small tree in python
class node:
    # initialize
    def __init__(self, inode):
        self.root = inode
        self.children = []
    # add childrens of type node
    def add_child(self, inode):
        self.children.append(inode)
    # get childrens of type node
    def get_children(self):
        return self.children
    # remove childrens of type node
    def remove_child(self, index_list):
        self.children.__delitem__(index_list)
    # print the root value of the node
    def print(self):
        print(self.root)
    # get the root value of the node
    def get_root(self):
        return self.root
    # set the root value of the node
    def set_root(self, inode):
        self.root = inode
    # get the value of a child node at a specific index
    def get_child_value(self, index_list):
        return self.children.__getitem__(index_list).get_root()
    # get the number of child nodes
    def get_child_count(self):
        return len(self.children)

# create root node
root= node(1)

# add child nodes to the root node
root.add_child(node(2))
root.add_child(node(3))

# print the child nodes of the root node
for i in root.get_children():
    print(i.get_root())
