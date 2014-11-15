class Solution:
    def __init__(self):
        self.memo = {}

    def foo(self, triangle, level, index):
        if (level, index) in self.memo:
            return self.memo[(level, index)]
        if triangle is None:
            return 0
        if level < 0 or level >= len(triangle):
            return 0
        if index < 0 or index >= len(triangle[level]):
            return 0
        l = self.foo(triangle, level+1, index)
        r = self.foo(triangle, level+1, index+1)

        self.memo[(level, index)] = min(l, r) + triangle[level][index]
        return self.memo[(level, index)]

    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        return self.foo(triangle, 0, 0)
