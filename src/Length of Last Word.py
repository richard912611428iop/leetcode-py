class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        parts = s.split()
        return len(parts[-1]) if len(parts) > 0 else 0
