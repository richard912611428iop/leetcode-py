class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None or len(A) == 0:
            return 0
        i = 0
        j = 0
        last_val = None
        while j < len(A):
            if last_val is None:
                last_val = A[j]
                j += 1
            else:
                if last_val != A[j]:
                    A[i+1] = A[j]
                    last_val = A[j]
                    i += 1
                    j += 1
                else:
                    j += 1
        return i + 1
