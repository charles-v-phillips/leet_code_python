from collections import Counter, defaultdict
import pprint
import string
# Time Limit Exceeded Error, not surprising
class Solution:
    def uniqueLetterString(self, s: str):
        total = 0
        for i in range(0,len(s)):
            for j in range(i+1,len(s) + 1):
                c = Counter(s[i:j])
                for k,v in c.items():
                    if v == 1:
                        total +=1

        return total

#Still get  a TLE
class Solution2:
    def uniqueLetterString(self, s : str):
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1


        for i  in range(n-2,-1,-1):
            for j in range(i+1,n):

                word = s[i:j]
                c = word.count(s[j])
                if c == len(word):
                    dp[i][j] = 0
                elif s[j] not in word:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    if c == 1:
                        dp[i][j] = dp[i][j-1] - 1
                    else:
                        dp[i][j] = dp[i][j-1]


        pprint.pprint(dp)
        tot = 0
        for i in range(n):
            for j in range(n):
                if i !=j:
                    tot+= dp[i][j]
        tot +=n
        return tot

class Solution3:
    def uniqueLetterString(self, s: str):
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        tot = n

        for i in range(n-2,-1,-1):
            d = defaultdict(int)
            d[s[i]] +=1
            for j in range(i+1,n):
                letter = s[j]

                if d[letter] == 0:
                    dp[i][j] = dp[i][j-1] + 1
                elif d[letter] == 1:
                    dp[i][j] = dp[i][j-1] - 1
                else:
                    dp[i][j] = dp[i][j-1]
                tot += dp[i][j]
                d[letter] += 1
        return tot

class Solution4:
    def uniqueLetterString(self, s: str):
        index = {c :[-1,-1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(s):
            k, j = index[c]
            res += (i-j)*(j-k)
            index[c] = [j,i]






if __name__ == '__main__':
    print(Solution3().uniqueLetterString("LEETCODE"))
    c = Counter('ETCODE')