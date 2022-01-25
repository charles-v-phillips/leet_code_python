options = ["1","2","3","4","5","6","7","8","9"]

class Solution(object):
    def __init__(self):
        self.empty_spots = list()


    def can_place(self,board,pos,option):
        x = pos[0]
        y = pos[1]
        for i in range(9):
            if board[x][i] == option:
                return False
            if board[i][y] == option:
                return False
        quadX = int(x/3)
        quadY = int(y/3)

        for i in range(3*quadX,3*quadX+3):
            for j in range(3*quadY,3*quadY+3):
                if board[i][j] == option:
                    return False

        return True

    def solve(self,pos,board):
        if(pos >= len(self.empty_spots)):
            print("Solution Found")
            for i in range(9):
                print(board[i])
            return True

        for option in options:
            if self.can_place(board,self.empty_spots[pos],option):
                x,y = self.empty_spots[pos][0], self.empty_spots[pos][1]
                board[x][y] = option
                if(self.solve(pos+1,board)):
                    return True
                else:
                    board[x][y] = "."





    def solveSudoku(self,board):
        self.empty_spots = [(i,j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == '.']
        return self.solve(0,board)



if __name__ == '__main__':

    b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    s.solve_sudoku(b)




