class Solution:
    def dfs(self, x, y, board, word):
        m = len(board)
        n = len(board[0])
        if word == "":
            return True
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if board[x][y] != word[0]:
            return False
        board[x][y] = '.'
        flag = False
        flag = flag or self.dfs(x-1, y, board, word[1:])
        flag = flag or self.dfs(x+1, y, board, word[1:])
        flag = flag or self.dfs(x, y-1, board, word[1:])
        flag = flag or self.dfs(x, y+1, board, word[1:])
        board[x][y] = word[0]
        return flag

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if word == "":
            return True
        flag = False
        for x in range(len(board)):
            for y in range(len(board[0])):
                flag = self.dfs(x, y, board, word)
                if flag:
                    return True
        return False
