class Solution:
    # @author KeiraTHU
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if len(s) == 0:
            return []
        length = len(s)
        s = s[::-1]
        state_table = []
        for i in range(length):
            tep = []
            if s[0: i+1] == s[i::-1]:
                tep.append([s[0:i+1]])
            for j in range(1, i+1):
                if s[j:i+1] == s[i:j-1:-1]:
                    for l in state_table[j-1]:
                        t = l[:]
                        t.append(s[j:i+1])
                        tep.append(t)
            state_table.append(tep)
        ret = state_table[-1]
        ret = [i[::-1] for i in ret]
        return ret
