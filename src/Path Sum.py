# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def foo(self, root, sum):
        if root is None:
            return False
        if sum == root.val and root.left is None and root.right is None:
            return True
        return self.foo(root.left, sum - root.val) or (
            self.foo(root.right, sum - root.val))

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.foo(root, sum)
