class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a = s.split()
        return " ".join(a[::-1])
