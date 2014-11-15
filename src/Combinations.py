class Solution:
    def dfs(self, n, k, start, cur, path, result):
        if cur == k:
            result.append(path[:])
        for i in range(start, n+1):
            path.append(i)
            self.dfs(n, k, i + 1, cur + 1, path, result)
            path.pop()
        return

    # @return a list of lists of integers
    def combine(self, n, k):
        path = []
        result = []
        self.dfs(n, k, 1, 0, path, result)
        return result
