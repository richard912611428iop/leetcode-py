class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return len(strs[0])
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:j]

        return strs[0]
