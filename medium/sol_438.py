from collections import defaultdict
from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        seen = defaultdict(int)
        anagram = Counter(p)
        n = len(s)
        l = r = 0
        rv = []
        while r < n:
            if anagram[s[r]] and seen[s[r]] + 1 <= anagram[s[r]]:
                seen[s[r]] += 1
                r += 1
                if seen == anagram:
                    rv.append(l)
                    seen[s[l]] -= 1
                    l += 1
            else:
                l += 1
                r = l
                seen.clear()
        return rv



if __name__ == '__main__':
    print(Solution().findAnagrams(s = "cbaebabacd", p = "abc"))


