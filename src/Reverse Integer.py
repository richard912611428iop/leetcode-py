class Solution:
    # @return an integer
    def reverse(self, x):
        minus_num = 1
        if x < 0:
            minus_num = -1
            x *= -1
        n = int("".join(reversed(list(str(x)))))
        return n * minus_num
