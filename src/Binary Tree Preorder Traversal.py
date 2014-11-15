# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.result = []

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is None:
            return []
        cur = root
        prev = None
        while cur:
            if cur.left is None:
                self.result.append(cur.val)
                prev = cur
                cur = cur.right
            else:
                prev = cur.left
                while prev.right is not None and prev.right != cur:
                    prev = prev.right
                if prev.right == cur:
                    prev.right = None
                    prev = cur
                    cur = cur.right
                else:
                    prev.right = cur
                    self.result.append(cur.val)
                    cur = cur.left
        return self.result
