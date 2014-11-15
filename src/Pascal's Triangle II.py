class Solution:
    # @lru_cache(maxsize = 100)
    def frac(self, num):
        if num < 0 or num == 0:
            return 1
        return num * self.frac(num-1)

    def cal(self, select, total):
        if select < 0 or select > total:
            return 0
        if select == 0 or select == total:
            return 1
        return self.frac(total) // (
            self.frac(total - select) * self.frac(select))

    # @return a list of integers
    def getRow(self, rowIndex):
        ret = []
        for i in range(rowIndex + 1):
            ret.append(self.cal(i, rowIndex))
        return ret
