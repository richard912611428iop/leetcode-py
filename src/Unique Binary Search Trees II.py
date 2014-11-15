# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def foo(self, start, end):
        if start >= end:
            yield None
            return
        for i in range(start, end):
            node = TreeNode(i+1)
            for l in self.foo(start, i):
                for r in self.foo(i+1, end):
                    node.left = l
                    node.right = r
                    yield node

    # @return a list of tree node
    def generateTrees(self, n):
        return list(map(copy.deepcopy, self.foo(0, n)))