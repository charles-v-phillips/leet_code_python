from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = max_window = 0
        seen = defaultdict(int)

        while r < len(s):
            if s[r] not in seen:
                if len(seen) == 2:
                    max_window = max(max_window, r - l)
                    #other stuff too
                    while len(seen) == 2:
                        seen[s[l]] -=1
                        if not seen[s[l]]:
                            del seen[s[l]]
                        l += 1
                    seen[s[r]] +=1
                    r += 1
                else:
                    seen[s[r]] += 1
                    r += 1


            else:
                seen[s[r]] += 1
                r += 1
        return max(max_window, r- l)



class Solution2:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = max_len = 0
        seen = defaultdict()

        while r < len(s):
            seen[s[r]] = r
            r += 1
            if len(seen) > 2:
                del_idx = min(seen.values())
                del seen[s[del_idx]]
                l = del_idx + 1
            max_len = max(max_len, r - l)
        return max_len



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringTwoDistinct(s = "ccaabbb"))
