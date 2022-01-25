from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        dp = [0 for _ in range(len(s))]
        d = defaultdict(int)
        d[s[0]] +=1
        dp[0] = 1
        for i in range(1,len(s)):
            letter = s[i]
            if d[letter] == 0:
                dp[i] = dp[i-1] + 1
            elif d[letter] == 1 :
                dp[i] = dp[i-1] - 1
            else:
                dp[i] = dp[i-1]
            d[letter] +=1
        return max(dp)

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window = set()
        max_window = 0
        left = 0
        right = 0

        while left < n and right < n:
            if s[right] not in window:
                window.add(s[right])
                right +=1

                max_window = max(max_window,right - left)

            else:
                window.remove(s[left])
                left +=1
        return max_window












if __name__ == '__main__':
    print(Solution2().lengthOfLongestSubstring(s = "abcabcbb"))