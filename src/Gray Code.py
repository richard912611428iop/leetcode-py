class Solution:
    def next_graycode(self, gray):
        if gray is None or len(gray) == 0:
            return ""
        ret = gray[:]
        rev_gray = reversed(gray)
        ret.extend(rev_gray)
        for i in range(len(ret)//2):
            ret[i] = "0"+ret[i]

        for i in range(len(ret)//2, len(ret)):
            ret[i] = "1"+ret[i]
        return ret

    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        inp = ["0", "1"]
        for i in range(n-1):
            inp = self.next_graycode(inp)
        ret = []
        for num in inp:
            ret.append(int(num, 2))
        return ret
