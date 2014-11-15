class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        low = 0
        high = len(num)-1
        while high - low > 1:
            mid = (low+high) // 2
            if num[mid] < num[high]:
                high = mid
            else:
                low = mid + 1
        return min(num[high], num[low])
