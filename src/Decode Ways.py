class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == "" or s == "0":
            return 0
        prev = 0
        cur = 1
        for i in range(1, len(s)+1):
            if s[i-1] == '0':
                cur = 0
            if i < 2 or int(s[i-2:i]) not in range(10, 27):
                prev = 0
            cur, prev = prev+cur, cur

        return cur
