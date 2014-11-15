# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.prev_node = None

    def foo(self, node):
        if node is None:
            return
        self.prev_node.right = node
        self.prev_node.left = None
        self.prev_node = node
        right_child = node.right
        self.foo(node.left)
        self.foo(right_child)
        return

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        dummy_node = TreeNode(0)
        dummy_node.right = root
        self.prev_node = dummy_node
        self.foo(root)
