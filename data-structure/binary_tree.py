class Node:
    def __init__(self, value=None, level=1):
        self.value = value
        self.level = level
        self.left = None
        self.right = None

    def add_next_node(self, value, level_here=2):
        new_node = Node(value, level_here)

        if value > self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right = self.right.add_next_node(value, level_here+1)

        elif value < self.value:
            if self.left is None:
                self.left = new_node
            else:
               self.left = self.left.add_next_node(value, level_here+1)

        return self


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.add_next_node(value)

BT = BinaryTree()
tlist = [6,4,8,2,5,7,9,1,3]

for i in tlist:
    BT.add_node(i)


