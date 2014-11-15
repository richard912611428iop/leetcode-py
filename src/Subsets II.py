class Solution:
    def __init__(self):
        self.iter_m = {}

    def foo(self, S):
        if S == [] or S is None:
            return [[]]
        num = S[0]
        dp_list = self.foo(S[1:])
        result_l = []
        for l in dp_list:
            new_l = l[:]
            if new_l not in result_l:
                result_l.append(new_l)
        for l in dp_list:
            new_l = l[:]
            new_l.insert(0, num)
            if new_l not in result_l:
                result_l.append(new_l)
        return result_l

    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S_sorted = sorted(S)
        return self.foo(S_sorted)
