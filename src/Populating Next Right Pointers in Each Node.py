# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def foo(self, node, silb):
        if node is None:
            return
        else:
            node.next = silb

        self.foo(node.left, node.right)
        if silb:
            self.foo(node.right, silb.left)
        else:
            self.foo(node.right, None)
        return

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        self.foo(root, None)
