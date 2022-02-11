from typing import List
import timeit

def generateParenthesis(n):
    def backtrack(S=[], left=0, right=0):
        if len(S) == 2 * n:
            rv.append(''.join(S))

        if left < n:
            S.append('(')
            backtrack(S,left + 1, right)
            S.pop()

        if right < left:
            S.append(')')
            backtrack(S, left ,right + 1)
            S.pop()



    rv = []
    backtrack()
    return rv


print(generateParenthesis(3))