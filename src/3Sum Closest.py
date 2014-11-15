class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        sorted_num = sorted(num)
        ret = 0
        min_gap = (1 << 31) - 1
        for ai in range(len(num)-2):
            a = sorted_num[ai]
            bi = ai+1
            ci = len(num)-1
            while bi < ci:
                b = sorted_num[bi]
                c = sorted_num[ci]
                total = a+b+c
                gap = abs(total - target)
                if gap < min_gap:
                    ret = total
                    min_gap = gap
                if total < target:
                    bi += 1
                else:
                    ci -= 1
        return ret
