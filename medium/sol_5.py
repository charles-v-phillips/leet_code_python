class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        max_palindrome = s[0]
        n = len(s)
        dp = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            dp[(i+1)%n][i] = True

        for i in range(n-2,-1,-1):
            for j in range(i + 1,n):
                dp[i][j] = ((s[i] == s[j]) and dp[i+1][j-1])
                if dp[i][j] and (j - i) + 1 > len(max_palindrome):
                    max_palindrome = s[i:j+1]

        return max_palindrome




if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd"))
    print(True and None)

