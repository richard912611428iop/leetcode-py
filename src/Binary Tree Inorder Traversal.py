# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root is None:
            return []
        prev = None
        cur = root
        ret = []
        while cur:
            if cur.left is None:
                ret.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right is not None and prev.right != cur:
                    prev = prev.right

                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    ret.append(cur.val)
                    cur = cur.right
        return ret
