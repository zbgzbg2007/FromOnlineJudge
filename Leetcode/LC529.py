class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i, j = click
        n, m = len(board[0]), len(board)
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        if board[i][j] != 'E':
            return board
        c = self.check(board, click)
        if c != 0:
            board[i][j] = str(c)
            return board
        else:
            board[i][j] = 'B'
            if i - 1 >= 0:
                self.updateBoard(board, [i-1, j])
                if j - 1 >= 0:
                    self.updateBoard(board, [i-1, j-1])
                if j + 1 < n:
                    self.updateBoard(board, [i-1, j+1])

            if j - 1 >= 0:
                self.updateBoard(board, [i, j-1])
            if j + 1 < n:
                self.updateBoard(board, [i, j+1])
            if i + 1 < m:
                self.updateBoard(board, [i+1, j])
                if j - 1 >= 0:
                    self.updateBoard(board, [i+1, j-1])
                if j + 1 < n:
                    self.updateBoard(board, [i+1, j+1])
        
        return board
        
    def check(self, board, click):
        i, j = click
        c = 0
        m, n = len(board), len(board[0])
        
        if i - 1 >= 0:
            if board[i-1][j] == 'M':
                c += 1
            if j - 1 >= 0 and board[i-1][j-1] == 'M':
                c += 1
            if j + 1 < n and board[i-1][j+1] == 'M':
                c += 1

        if j - 1 >= 0 and board[i][j-1] == 'M':
            c += 1
        if j + 1 < n and board[i][j+1] == 'M':
            c += 1
        if i + 1 < m:
            if board[i+1][j] == 'M':
                c += 1
            if j - 1 >= 0 and board[i+1][j-1] == 'M':
                c += 1
            if j + 1 < n and board[i+1][j+1] == 'M':
                c += 1
        return c
            
       
