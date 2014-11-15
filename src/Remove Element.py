class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if A is None or len(A) == 0:
            return 0
        i = 0
        j = 0
        while j < len(A):
            if A[j] == elem:
                j += 1
            else:
                A[i] = A[j]
                i += 1
                j += 1
        return i
