
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        moves = [[0,1],[1,0]]
        self.min_health = float('inf')

        def dfs(x,y,hg,hl):
            if dungeon[x][y] > 0: hg += dungeon[x][y]
            else: hl += abs(dungeon[x][y])

            if x == len(dungeon)-1 and y == len(dungeon[0])-1:
                self.min_health = min(self.min_health, abs(hg - hl))

            for move in moves:
                next_x = x + move[0]
                next_y = y + move[1]
                if next_x < len(dungeon) and next_y < len(dungeon[0]):
                    dfs(next_x,next_y,hg,hl)








        dfs(0,0,0,0)

        return 1 + self.min_health

if __name__ == '__main__':
    print(Solution().calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]))

