from collections import defaultdict
# messy solution that works
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = max_window = 0
        n = len(s)
        window = set()
        last_occurrence = defaultdict(int)

        while l <= r < n:
            if len(window) < 2:
                window.add(s[r])
                last_occurrence[s[r]] = r
                r +=1
                max_window = max(max_window, r-l)
            elif len(window) == 2 and s[r] in window:
                last_occurrence[s[r]] = r
                r += 1
                max_window = max(max_window, r-l)
            else:
                el_to_remove = s[l]
                l += 1
                if last_occurrence[el_to_remove] < l:
                    window.remove(el_to_remove)
        return max_window

class Solution2:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        l = r = max_window = 0
        most_recent_occurrence = defaultdict(int)

        while r < n:
            most_recent_occurrence[s[r]] = r
            r += 1
            if len(most_recent_occurrence) > 2:
                del_idx = min(most_recent_occurrence.values())
                del most_recent_occurrence[s[del_idx]]
                l = del_idx + 1
            max_window = max(max_window, r-l)
        return max_window





if __name__ == '__main__':
    print(Solution2().lengthOfLongestSubstringTwoDistinct(s = "cdaba"))
