class Solution:
    # @powered makeittrue(https://oj.leetcode.com/discuss/user/makeittrue)
    # @return an integer
    def romanToInt(self, s):
        ret = 0
        s = reversed(s)
        for c in s:
            if c == 'I':
                ret += -1 if ret >= 5 else 1
            elif c == 'V':
                ret += 5
            elif c == 'X':
                ret += 10 * -1 if ret >= 50 else 10
            elif c == 'L':
                ret += 50
            elif c == 'C':
                ret += 100 * -1 if ret >= 500 else 100
            elif c == 'D':
                ret += 500
            elif c == 'M':
                ret += 1000
        return ret
