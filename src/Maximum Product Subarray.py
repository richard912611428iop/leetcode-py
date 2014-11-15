class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return A[0]
        ret = 0
        acc = 1
        for i in range(len(A)):
            if A[i] == 0:
                acc = 1
                continue
            acc *= A[i]
            ret = max(acc, ret)

        acc = 1
        for i in range(len(A)-1, -1, -1):
            if A[i] == 0:
                acc = 1
                continue
            acc *= A[i]
            ret = max(acc, ret)
        return ret
