class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        flag = 0
        for i in range(32):
            flag = 1 << i
            count = 0
            for a in A:
                if a & flag == flag:
                    count += 1
            if count % 3 != 0:
                result |= flag
        return result if result < 1 << 31 else result - (1 << 32)
