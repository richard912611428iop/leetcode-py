# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def foo(self, root, lower, upper):
        if root is None:
            return True
        return (root.val > lower and root.val < upper and
                self.foo(root.left, lower, root.val) and
                self.foo(root.right, root.val, upper))

    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if root is None:
            return True
        return self.foo(root, -1 << 31, 1 << 31)
