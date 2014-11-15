class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        f = [False for i in range(len(s)+1)]
        f[0] = True
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if f[j] and s[j:i] in dict:
                    f[i] = True
                    break
        return f[len(s)]
