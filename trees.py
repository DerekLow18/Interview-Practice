'''
This file will be about trees, primarily the construction and search
of trees.

The tree data structure is normally represented as a root node with
a series of child nodes that grow downward from the root node, forming
a tree-like structure. Every node in the tree can have 0 or more
children, and trees that have two nodes at maximum (typically
a left and right node) are called binary trees.

Here, we have the binary search tree implementation.


'''
#small node object
class node(object):

    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

#search tree object
class BST(object):

    def __init__(self):
        self.top = None

    def sortArrayToBST(self,array):
        if not array:
            return
        mid = len(array)/2
        root = node(array[mid])
        root.leftchild = self.sortArrayToBST(array[0:mid])
        root.rightchild = self.sortArrayToBST(array[mid+1:len(array)+1])

    def printTree(self, node):
        if node != None:
            self.printTree(node.leftchild)
            print(node.value)
            self.printTree(node.rightchild)

#generate a series of random numbers to organize into the tree
if __name__ == "__main__":
    myArray = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    bst = node(myArray)
    bst.printTree(bst)


    




