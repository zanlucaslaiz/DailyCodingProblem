"""

EASY

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
class NodeTree:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.key,
                                    self.key,
                                    self.right and self.right.key)
    


root = NodeTree(8)
root.left = NodeTree(2)
root.right  = NodeTree(8)
print("Tree: ", root)