import collections
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def generate_neighbors(combo):
            neighbors = []
            for i,c in enumerate(combo):
                neighbors.append(combo[:i] + str((int(c) + 1) % 10) + combo[i+1:])
                neighbors.append(combo[:i] + str((int(c) - 1) % 10) + combo[i+1:])
            return neighbors


        start = '0000'
        if start in deadends:
            return -1
        q = collections.deque()
        q.append(start)
        depth = 0
        seen  = set()
        seen.add(start)




        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node == target:
                    return depth
                neighbors = generate_neighbors(node)
                for neighbor in neighbors:
                    if neighbor not in deadends and neighbor not in seen:
                        q.append(neighbor)
                        seen.add(neighbor)

            depth += 1


        return -1








if __name__ == '__main__':
    print(Solution().openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
    print(Solution().openLock(deadends = ["8888"], target = "0009"))
    print(Solution().openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
