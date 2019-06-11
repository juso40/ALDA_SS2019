import random
class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None



class SearchTree():
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def insert(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
        elif

    def remove(self, key):
        if

    def find(self, key):
        pass # your code here

tree = SearchTree()

for i in range(0, 100):
    tree.insert(random.randint(0, 100), random.randint(0, 100000000))
for Nodes in tree._myNodes[1:]:
    print("Key:", Nodes.key, "Value:", Nodes.value)
