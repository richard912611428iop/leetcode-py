class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = matrix[-1]
        for i in range(len(matrix)):
            if matrix[i][0] < target:
                continue
            elif matrix[i][0] == target:
                return True
            else:
                row = matrix[i-1]
                break
        for n in row:
            if n == target:
                return True
        return False
