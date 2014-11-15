class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        new_s = []
        for c in s:
            if c in ("0123456789abcdefghijklmnopqrstuvwxyz"):
                new_s.append(c)
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-i-1]:
                return False
        return True
