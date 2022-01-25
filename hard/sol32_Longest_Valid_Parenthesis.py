class Solution:
    def longestValidParentheses(self, s: str) -> int:

        while True:
            if s[0] == '(':
                break
            else: s = s[1:]

        while True:
            if s[-1] == ')':
                break
            else:
                s = s[:-1]

        n = len(s)
        print(s)







if __name__ == '__main__':
    Solution().longestValidParentheses("))()()")
    for i in range(20):
        print(i)


