# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)

        return min(l, r) + 1 if min(l, r) > 0 else max(l, r) + 1
