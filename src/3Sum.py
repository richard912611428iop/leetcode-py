class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        sorted_num = sorted(num)
        target = 0
        ret = []
        a = None
        for ai in range(len(num)-2):
            last_b = None
            if sorted_num[ai] == a:
                continue
            a = sorted_num[ai]
            bi = ai+1
            ci = len(num)-1
            while bi < ci:
                b = sorted_num[bi]
                c = sorted_num[ci]
                if a + b + c > target:
                    ci -= 1
                else:
                    if last_b == sorted_num[bi]:
                        bi += 1
                        continue
                    last_b = b
                    if a + b + c == 0:
                        ret.append([a, b, c])
                    bi += 1
        return ret
