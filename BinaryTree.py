class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def InsertNode(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.InsertNode(data)
                else:
                    self.left = Node(data)
            elif self.data < data:
                if self.right:
                    self.right.InsertNode(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

        # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def FindVal(self, data):
        if self.data > data:
            if self.left is None:
                return f'{data} Not Found'
            return self.left.FindVal(data)
        elif self.data < data:
            if self.right is None:
                return f'{data} Not Found'
            return self.right.FindVal(data)
        else:
            return f'{data} Found'


root = Node(10)
for i in range(5, 15):
    root.InsertNode(i)

#root.PrintTree()
print (root.FindVal(111))
print (root.FindVal(11))


