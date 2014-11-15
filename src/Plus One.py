class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        res_stack = []
        rest = 1
        for i in range(len(digits)-1, -1, -1):
            res_stack.append((rest + digits[i]) % 10)
            rest = (rest + digits[i]) // 10
        if rest == 1:
            res_stack.append(rest)
        return list(reversed(res_stack))
