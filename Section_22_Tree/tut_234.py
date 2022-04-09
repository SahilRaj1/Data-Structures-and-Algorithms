""" Binary Tree using List """

class BinaryTree:
    def __init__(self, size):
        self.list = size * [None]
        self.index = 0
        self.maxSize = size

    # Inserting in Binary Tree
    def insert(self, value):
        if self.index + 1 == self.maxSize:
            print("The Binary Tree is full")
        else:
            self.list[self.index+1] = value
            self.index += 1
            return

    # Searching in Binary Tree
    def search(self, value):
        for i in range(1, self.index+1):
            if self.list[i] == value:
                return True
        return False

    # Pre Order Traversal in Binary Tree
    def preOrderTraversal(self, index):
        if index > self.index:
            return
        else:
            print(self.list[index])
            self.preOrderTraversal(index*2)
            self.preOrderTraversal(index*2 + 1)

    # In Order Traversal in Binary Tree
    def inOrderTraversal(self, index):
        if index > self.index:
            return
        else:
            self.inOrderTraversal(index*2)
            print(self.list[index])
            self.inOrderTraversal(index*2 + 1)

    # Post Order Traversal in Binary Tree
    def postOrderTraversal(self, index):
        if index > self.index:
            return
        else:
            self.postOrderTraversal(index * 2)
            self.postOrderTraversal(index * 2 + 1)
            print(self.list[index])

    # Level Order Traversal in Binary Tree
    def levelOrderTraversal(self):
        for i in range(1, self.index+1):
            print(self.list[i])
        return

    # Deleting a node from Binary Tree
    def delete(self,value):
        if self.index == 0:
            print("The Binary Tree is empty")
        for i in range(1, self.index+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.index]
                self.list[self.index] = None
                self.index -= 1
        return

    # Deleting entire Binary Tree
    def deleteBT(self):
        self.list = None
        return


# Creating Binary Tree
newBT = BinaryTree(10)

# Inserting
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")

# Searching
# print(newBT.search("Drinks"))

# Pre Order Traversal
# newBT.preOrderTraversal(1)

# In Order Traversal
# newBT.inOrderTraversal(1)

# Pre Order Traversal
# newBT.postOrderTraversal(1)

# Level Order Traversal
# newBT.levelOrderTraversal()

# Deleting a node
newBT.delete("Hot")
# newBT.levelOrderTraversal()

# Deleting entire BT
newBT.deleteBT()
