from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = r = max_len = 0
        d = defaultdict(int)

        while r < len(s):
            d[s[r]] = r
            r +=1
            if len(d) > k:
                del_idx = min(d.values())
                del d[s[del_idx]]
                l = del_idx + 1
            max_len = max(max_len, r - l)
        return max_len

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct(s = "aa", k = 1))