class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            valid_l = {'9': 1, '1': 1, '2': 1,
                       '3': 1, '4': 1, '5': 1,
                       '6': 1, '7': 1, '8': 1, '.': 9}
            for j in range(9):
                if valid_l[board[i][j]] >= 1:
                    valid_l[board[i][j]] -= 1
                else:
                    return False

        for j in range(9):
            valid_l = {'9': 1, '1': 1, '2': 1,
                       '3': 1, '4': 1, '5': 1,
                       '6': 1, '7': 1, '8': 1, '.': 9}
            for i in range(9):
                if valid_l[board[i][j]] >= 1:
                    valid_l[board[i][j]] -= 1
                else:
                    return False

        for i in range(3):
            for j in range(3):
                valid_l = {'9': 1, '1': 1, '2': 1,
                           '3': 1, '4': 1, '5': 1,
                           '6': 1, '7': 1, '8': 1, '.': 9}
                for row in range(i*3, i*3+3):
                    for col in range(j*3, j*3+3):
                        if valid_l[board[row][col]] >= 1:
                            valid_l[board[row][col]] -= 1
                        else:
                            return False
        return True
