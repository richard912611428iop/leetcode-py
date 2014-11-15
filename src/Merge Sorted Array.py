class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        j = 0
        while i < m and n > 0:
            if A[i] < B[j]:
                while i < m and A[i] < B[0]:
                    i += 1
                A.insert(i, B.pop(0))
                m += 1
                n -= 1
            else:
                while n > 0 and A[i] >= B[0]:
                    A.insert(i, B.pop(0))
                    n -= 1
                    m += 1
        while len(B) > 0:
            A.insert(m + n - len(B), B.pop(0))
        return
