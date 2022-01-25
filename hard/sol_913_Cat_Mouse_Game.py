from typing import List
from enum import Enum

class Solution2:
    def catMouseGame(self, graph: List[List[int]]) -> int:

        seen = [[[False] * 2 for _ in range(len(graph))] for _ in range(len(graph))]
        memo = [[[-1] * 2 for _ in range(len(graph))] for _ in range(len(graph))]

        def is_terminal(cat, mouse):
            return mouse == cat or mouse == 0

        def minimize(cat, mouse, turn):
            if is_terminal(cat, mouse):
                return 2 if mouse == 0 else 0

            if seen[cat][mouse][turn]:
                return 1
            if memo[cat][mouse][turn] >= 0:
                return memo[cat][mouse][turn]

            seen[cat][mouse][turn] = True

            v = min(maximize(c,mouse, (turn + 1)%2) for c in graph[cat] if c != 0)
            memo[cat][mouse][turn] = v
            seen[cat][mouse][turn] = False
            return v

        def maximize(cat, mouse,turn):
            if is_terminal(cat,mouse):
                return 2 if mouse == 0 else 0
            if seen[cat][mouse][turn]:
                return 1
            if memo[cat][mouse][turn] >= 0:
                return memo[cat][mouse][turn]

            seen[cat][mouse][turn] = True

            v = max(minimize(cat, m,(turn + 1)%2) for m in graph[mouse])
            memo[cat][mouse][turn] = v
            seen[cat][mouse][turn] = False
            return v

        def minimax(cat,mouse):
            return max(minimize(cat,m, 0) for m in graph[mouse])

        results = {0: 2, # mouse loses
                   1: 0, #draw
                   2: 1} # mouse wins
        return results[minimax(2,1)]

class Solution3:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        seen = [[[False] * 2 for _ in range(len(graph))] for _ in range(len(graph))]
        memo = [[[-1] * 2 for _ in range(len(graph))] for _ in range(len(graph))]

        def is_terminal(cat, mouse):
            return mouse == cat or mouse == 0

        def minimax(cat, mouse, turn):
            if is_terminal(cat,mouse):
                return 2 if mouse == 0 else 0
            if seen[cat][mouse][turn]:

                memo[cat][mouse][turn] = 1
                return 1
            if memo[cat][mouse][turn] >= 0:
                return memo[cat][mouse][turn]

            seen[cat][mouse][turn] = True

            if turn == 0:
                v = max(minimax(cat,m, 1) for m in graph[mouse])
            if turn == 1:
                v = min(minimax(c,mouse,0) for c in graph[cat] if c != 0)

            # memo[cat][mouse][turn] = v
            seen[cat][mouse][turn] = False
            return v

        results = {0: 2,  # mouse loses
                   1: 0,  # draw
                   2: 1}  # mouse wins
        return results[minimax(2, 1,0)]






if __name__ == '__main__':
    print(Solution3().catMouseGame(graph=[[1, 3], [0], [3], [0, 2]])) #1
    print(Solution3().catMouseGame(graph=[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]])) #0
    print(Solution3().catMouseGame(graph=[[4], [2, 3, 5], [1, 5, 3], [1, 2], [0], [1, 2]])) #2
    print(Solution3().catMouseGame(graph=[[2,6],[2,4,5,6],[0,1,3,5,6],[2],[1,5,6],[1,2,4],[0,1,2,4]])) #TLE
    print(Solution2().catMouseGame(graph=[[5,6],[3,4],[6],[1,4,5],[1,3,5],[0,3,4,6],[0,2,5]])) # 2






