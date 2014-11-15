# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None:
            return []
        if sum - root.val != 0 and root.left is None and root.right is None:
            return []
        if sum == root.val and (root.left is None and root.right is None):
            return [[root.val]]

        ret = []
        left_ret = self.pathSum(root.left, sum-root.val)
        right_ret = self.pathSum(root.right, sum-root.val)
        if left_ret is not None:
            for i in left_ret:
                i.insert(0, root.val)
                ret.append(i)
        if right_ret is not None:
            for i in right_ret:
                i.insert(0, root.val)
                ret.append(i)
        return ret
