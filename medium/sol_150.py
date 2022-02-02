from typing import List
from operator import add, floordiv, mul, sub, truediv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integer_stack = []
        operators = {'+' : add,
                     '-' : sub,
                     '*' : mul,
                     '/' : truediv}


        for token in tokens:

            if token in operators:
                e2 = integer_stack.pop()
                e1 = integer_stack.pop()
                result = int(operators[token](e1,e2))
                integer_stack.append(result)
            else:
                integer_stack.append(int(token))

        return integer_stack[0]

if __name__ == '__main__':
    # print(Solution().evalRPN(tokens = ["2","1","+","3","*"]))
    print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))





