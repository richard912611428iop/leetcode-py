# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def foo(self, root):
        if root is None:
            return 0
        l = self.foo(root.left)
        r = self.foo(root.right)
        if abs(l - r) <= 1 and l != -2 and r != -2:
            return max(l, r) + 1
        else:
            return -2

    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.foo(root) != -2
