class Solution:
    def solveSudoku(self, board) -> None:
        moves = '123456789'
        open_spots = [[i,j] for i in range(9) for j in range(9) if board[i][j] == '.']
        directions = [[0,1],[0,-1],[1,0], [-1,0]]
        def can_place(move,x,y):
            for dx,dy in directions:
                sx = x + dx
                sy = y + dy
                while 0 <= sx < 9 and 0 <= sy < 9:
                    if board[sx][sy] == move:
                        return False
                    sx += dx
                    sy += dy

            xq = (x//3)*3
            yq = (y//3)*3
            for i in range(xq,xq+3):
                for j in range(yq,yq+3):
                    if board[i][j] == move:
                        return False
            return True

        def helper(depth):
            if depth == len(open_spots):
                return True
            x,y = open_spots[depth]
            for move in moves:
                if can_place(move, x,y):
                    board[x][y] = move
                    if helper(depth + 1):
                        return True
                    else:
                        board[x][y] = '.'



            return False

        helper(0)





if __name__ == '__main__':
    print(Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],
                                          ["6",".",".","1","9","5",".",".","."],
                                          [".","9","8",".",".",".",".","6","."],
                                          ["8",".",".",".","6",".",".",".","3"],
                                          ["4",".",".","8",".","3",".",".","1"],
                                          ["7",".",".",".","2",".",".",".","6"],
                                          [".","6",".",".",".",".","2","8","."],
                                          [".",".",".","4","1","9",".",".","5"],
                                          [".",".",".",".","8",".",".","7","9"]]))