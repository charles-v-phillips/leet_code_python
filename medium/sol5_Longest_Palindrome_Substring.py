class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.largest_palindrome = ""
        def is_palindrome(s):
            return s == s[::-1]
        def helper(lower,upper):
            if upper <= len(s) and is_palindrome(s[lower:upper]):
                if upper - lower > len(self.largest_palindrome):
                    self.largest_palindrome = s[lower:upper]
            if upper >len(s) or lower > upper:
                return

            helper(lower,upper+1)
            helper(lower+1,upper)


        helper(0,0)
        return self.largest_palindrome

class Solution2:
    def longestPalindrome(self,s):
        dp = [[None]*(len(s)+1) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            dp[i][i+1] = s[i]==s[i+1] if i != len(s)-1 else s[i] == s[i-1]

        for i in range(len(s)):
            for j in range(i+2,len(dp)):
                dp[i][j] = True if dp[i+1][j-1] == True and s[i] == s[j] else False

        largest = ""
        for i in range(len(dp)):
            for j in range(i,len(dp)):
                if dp[i][j]:
                    if len(s[i:j+1]) > len(largest):
                        largest = s[i:j+1]
        return largest


    def try2(self,s):
        n = len(s)
        dp = [[None]*n for _ in range(n)]

        largest_palindrome = s[0]
        for i in range(n):
            dp[i][i] = True
            if i != n-1:
                dp[i][i+1] = s[i] == s[i+1]
                if dp[i][i+1]:
                    largest_palindrome = s[i:i+2]





        for i in range(n-3,-1,-1):
            for j in range(i+2,n):
                dp[i][j] = True if dp[i+1][j-1] and s[i] == s[j] else False
                if dp[i][j] and len(largest_palindrome) < j+1 - i:
                    largest_palindrome = s[i:j+1]


        return largest_palindrome








if __name__ == '__main__':
    print(Solution2().try2("cbbd"))