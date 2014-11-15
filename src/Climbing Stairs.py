class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = [0 for i in range(n)]
        if n == 1:
            return 1
        if n == 2:
            return 2
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]
        return f[n - 1]
