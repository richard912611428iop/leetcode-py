class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ret = A[0]
        for i in range(1, len(A)):
            ret ^= A[i]
        return ret
