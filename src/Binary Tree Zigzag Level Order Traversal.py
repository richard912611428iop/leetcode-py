# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.levels = []

    def foo(self, node, level):
        if node is None:
            return
        while level > len(self.levels):
            self.levels.append([])
        if level % 2 != 1:
            self.levels[level-1].insert(0, node.val)
        else:
            self.levels[level-1].append(node.val)
        self.foo(node.left, level+1)
        self.foo(node.right, level+1)
        return

    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        self.foo(root, 1)
        return self.levels
