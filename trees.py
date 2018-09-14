'''
This file will be about trees, primarily the construction and search
of trees.

The tree data structure is normally represented as a root node with
a series of child nodes that grow downward from the root node, forming
a tree-like structure. Every node in the tree can have 0 or more
children, and trees that have two nodes at maximum (typically
a left and right node) are called binary trees.


'''

class node:

    def __init__(self,value, level, max_children = 2):
        self.value = value
        self.level = level
        self.max_children = 2
        self.children = []


    def addNode(self, value):
        child = node(value)
        self.children.append(child)

    



