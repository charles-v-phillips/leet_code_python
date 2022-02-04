from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, partial):
            if len(partial) == k:
                res.append(partial)
                return

            for e in range(start, n + 1):
                backtrack(e + 1, partial + [e])

        backtrack(1,[])
        return res

if __name__ == '__main__':
    print(Solution().combine(4,2))


