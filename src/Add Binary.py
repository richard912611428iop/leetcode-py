class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        res_stack = []
        i = 1
        j = 1
        rest = 0
        while i < len(a)+1 and j < len(b)+1:
            res_stack.append((rest + int(a[-i]) + int(b[-j])) % 2)
            rest = (rest + int(a[-i]) + int(b[-j])) // 2
            i += 1
            j += 1
        while i < len(a) + 1:
            res_stack.append((rest + int(a[-i])) % 2)
            rest = (rest + int(a[-i])) // 2
            i += 1
        while j < len(b) + 1:
            res_stack.append((rest + int(b[-j])) % 2)
            rest = (rest + int(b[-j])) // 2
            j += 1
        if rest == 1:
            res_stack.append(1)
        return "".join(list(map(str, reversed(res_stack))))
