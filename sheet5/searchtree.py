class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class SearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self,key, value):
        #First we initialize a root
        if self.root == None:
            self.root = Node(key, value)
            self.size += 1
            return self
        #Now we need to iterate trough our Tree to find the new Nodes location
        tempNode = self.root
        while True:
            if key == tempNode.key:     #We do want to replace our Nodes value if they do have the same 
                tempNode.value = value
                return self
            #Either the New key is smaller
            elif key < tempNode.key:
                if tempNode.left == None:
                    tempNode.left = Node(key, value)    #We only want to add the node here if the left side is empy
                    self.size += 1
                    return self
                tempNode = tempNode.left    #We change our tempNode and continue with the search for its place
            #or the new key is bigger
            elif key > tempNode.key:
                if tempNode.right == None:
                    tempNode.right = Node(key, value)
                    self.size += 1
                    return self
                tempNode = tempNode.right


    def remove(self, key):
        if self.root is None:
            raise KeyError ("No such key in this tree!")
            return None
        if key == self.root.key:
            tempNodeL = self.root.left
            tempNodeR = self.root.right
            self.root = Node(None, None)
            self.root.left = tempNodeL
            self.root.right = tempNodeR
            return print("You removed the root! The root is now None!")   
        while True:
            tempNode = self.root
            if key < tempNode.key:
                tempNode = tempNode.left
                continue
            if key > tempNode.key:
                tempNode = tempNode.right
                continue
    def find(self, key):
        pass


#a)
tree = SearchTree()
tree.insert(7, 'Root')
tree.insert(4, 'Left1')
tree.insert(5, 'Right1')
