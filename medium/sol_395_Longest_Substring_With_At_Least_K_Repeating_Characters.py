from collections import defaultdict
import numpy as np
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        r = l = max_window = 0
        window = defaultdict(int)
        n = len(s)

        while r < n:
            window[s[r]] +=1

    def ameoba(self,initial_pop, time_steps):

        total_pop = initial_pop
        pops = [initial_pop]
        for t in range(time_steps):
            for amoeba in range(total_pop):
                x = np.random.uniform(0, 1)
                if x < .25:
                    total_pop -= 1
                elif .25 <= x < .5:
                    total_pop = total_pop
                elif .5 <= x < .75:
                    total_pop += 1
                else:
                    total_pop += 2
            pops.append(total_pop)
            if total_pop <= 0:
                return pops
        return pops

if __name__ == '__main__':
    Solution().ameoba(1,3)