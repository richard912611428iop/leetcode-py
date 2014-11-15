class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i = 0
        j = 0
        k = 0
        for c in A:
            if c == 0:
                A[i] = 2
                i+=1
                A[j] = 1
                j+=1
                A[k] = 0
                k+=1
            elif c == 1 :
                A[i] = 2
                i+=1
                A[j] = 1
                j+=1
            elif c == 2:
                A[i] = 2
                i+=1

        return 
