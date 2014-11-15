class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        d = 1
        while x / d >= 10:
            d *= 10

        while x > 0:
            q = x // d
            r = x % 10
            if q != r:
                return False
            x = x % d / 10
            d /= 100
        return True
