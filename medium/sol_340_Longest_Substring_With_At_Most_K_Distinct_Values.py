from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        l = r = max_window = 0
        n = len(s)
        most_recent_occurrence = defaultdict()

        while r < n:
            most_recent_occurrence[s[r]] = r
            r +=1
            if len(most_recent_occurrence) > k:
                idx_to_delete = min(most_recent_occurrence.values())
                del most_recent_occurrence[s[idx_to_delete]]
                l = idx_to_delete + 1
            max_window = max(max_window,r-l)
        return max_window




if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct(s = "ab", k = 1))


