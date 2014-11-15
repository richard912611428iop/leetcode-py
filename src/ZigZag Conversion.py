class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows < 2 or len(s) < nRows:
            return s
        return_str = []
        for row in range(nRows):
            if row == 0 or row == nRows - 1:
                step = 2 * nRows - 2
                index = row
                while index < len(s):
                    return_str.append(s[index])
                    index += step
            else:
                step = 2 * nRows - 2
                index = row
                while index < len(s):
                    return_str.append(s[index])
                    zig_index = index + (step - 2*row)
                    if zig_index < len(s):
                        return_str.append(s[zig_index])
                    index += step
        return "".join(return_str)
