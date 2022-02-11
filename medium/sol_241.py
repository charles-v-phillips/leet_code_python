import string
from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        rv = []
        def helper(index, partial):
            if index == len(expression):
                rv.append(partial + ')')

            for i in range(index, len(expression)):
                if expression[i] in string.digits:
                    helper(index + 1, partial + ')' + expression[i])
                    helper(index + 1, partial + expression[i] + '(')
                else:
                    helper(index + 1, partial + expression[i])

        helper(0,'(')
        return rv

from operator import add, sub, mul
class Solution2:
    def diffWaysToCompute(self, expression: str) -> List:
        op_dict = {'+' : add, '-' : sub, '*' : mul}
        rv = []
        def dfs(index,partial):
            if '+' not in partial and '-' not in partial and '*' not in partial:
                rv.append(partial)
                return

            for i in range(len(partial)):
                if expression[i] in op_dict:
                    op = op_dict[partial[i]]
                    int1 = int(partial[i - 1])
                    int2 = int(partial[i + 1])
                    result = str(op(int1, int2))
                    dfs(index + 1, partial[:i-1] + result + partial[i+2:])


        dfs(0,expression)
        return rv

class Solution3:
    def diffWaysToCompute(self, expression: str) -> List:
        op_dict = {'+': add, '-': sub, '*': mul}
        def parse(s):
            rv = []
            i = 0
            num = ''
            while i < len(s):
                if s[i] in op_dict:
                    rv.append(int(num))
                    rv.append(s[i])
                    num = ''
                else:
                    num += s[i]
                i += 1
            rv.append(int(num))
            return rv


        def dfs(arr):
            if len(arr) == 1:
                rv.append(arr[0])
                return
            for i, e in enumerate(arr):
                if e in op_dict:
                    int1 = arr[i - 1]
                    int2 = arr[i + 1]
                    op = op_dict[e]
                    result = op(int1,int2)
                    dfs(arr[:i - 1] + [result] + arr[i + 2:])


        rv = []
        arr = parse(expression)
        dfs(arr)
        return rv




if __name__ == '__main__':
    print(Solution3().diffWaysToCompute("2*3-4*5"))











