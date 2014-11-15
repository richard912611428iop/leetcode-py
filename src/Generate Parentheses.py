class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        ret = []
        for i in range(n):
            inside = self.generateParenthesis(i)
            outside = self.generateParenthesis(n-1-i)
            for a in inside:
                for b in outside:
                    ret.append('('+a+')'+b)
        return ret
