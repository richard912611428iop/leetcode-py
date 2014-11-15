class Solution:
    def foo(self, data, maxlen):
        L = []
        for i in range(maxlen):
            data = "".join(str(len(list(g)))+str(n) for n, g in (
                itertools.groupby(data)))
            L.append(data)
        return L

    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        ret = self.foo("1", n-1)
        return ret[-1]
