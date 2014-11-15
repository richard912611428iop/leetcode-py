class Solution:
    def dfs(self, s, solutions, results, step):
        if step == 4 and len(s) == 0:
            results.append(".".join(solutions[:]))
            return
        if len(s) > 3*(4-step) or len(s) < 4-step:
            return
        if int(s[-3:]) in range(100, 256):
            solutions.insert(0, s[-3:])
            self.dfs(s[:-3], solutions, results, step+1)
            solutions.pop(0)
        if int(s[-2:]) in range(10, 100):
            solutions.insert(0, s[-2:])
            self.dfs(s[:-2], solutions, results, step+1)
            solutions.pop(0)
        if int(s[-1:]) in range(0, 10):
            solutions.insert(0, s[-1:])
            self.dfs(s[:-1], solutions, results, step+1)
            solutions.pop(0)
        return

    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        solution = []
        results = []
        self.dfs(s, solution, results, 0)
        return results
