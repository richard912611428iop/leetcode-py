class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_m = {}
        for i in range(len(num)):
            if num[i] not in num_m:
                num_m[num[i]] = i
        for i in range(len(num)):
            n = num[i]
            if target - n in num_m:
                if target - n == n:
                    if num.count(n) != 1:
                        r1 = num.index(n)
                        return r1 + 1, num.index(n, r1 + 1) + 1
                    else:
                        continue
                if num_m[n] > num_m[target - n]:
                    return num_m[target - n]+1, num_m[n]+1
                else:
                    return num_m[n]+1, num_m[target - n]+1
