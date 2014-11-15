# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        length = len(num)
        if length == 0:
            return None
        root =  TreeNode(num[length // 2])
        root.left = self.sortedArrayToBST(num[0: length // 2])
        root.right = self.sortedArrayToBST(num[length // 2 + 1: length])
        return root
