# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def foo(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        return node1.val == node2.val and (
            self.foo(node1.left, node2.right) and (
                self.foo(node1.right, node2.left)))

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        node1 = root.left
        node2 = root.right
        return node1.val == node2.val and (
            self.foo(node1.left, node2.right) and (
                self.foo(node1.right, node2.left)))
