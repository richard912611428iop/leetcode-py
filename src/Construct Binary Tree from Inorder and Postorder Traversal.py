# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        cur = postorder.pop(-1)
        root = TreeNode(cur)
        for i in range(len(inorder)):
            if inorder[i] == cur:
                root.right = self.buildTree(inorder[i+1:], postorder)
                root.left = self.buildTree(inorder[:i], postorder)
                break
        return root
