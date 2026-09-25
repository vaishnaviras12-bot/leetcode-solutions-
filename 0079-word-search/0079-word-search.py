class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        colomn =  len(board[0])

        def dfs(r,c,index):

            if r<0 or r>= len(board) or c<0 or c>=len(board[0]):
                return False

            if board[r][c]!= word[index]:
                return False

            if index == len(word) -1:
                return True

            original = board[r][c]
            board[r][c]= "#"

            directions = (dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1))
            board[r][c] = original
            return directions
                
        
        for i in range (row):
            for j in range(colomn):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True

        return False
        