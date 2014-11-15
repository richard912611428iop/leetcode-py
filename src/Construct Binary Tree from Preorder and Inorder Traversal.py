# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root_in_pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: 1+root_in_pos],
                                   inorder[: root_in_pos])
        root.right = self.buildTree(preorder[1+root_in_pos:],
                                    inorder[root_in_pos+1:])
        return root
