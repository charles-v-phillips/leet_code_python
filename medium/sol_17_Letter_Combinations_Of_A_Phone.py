from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2' : 'abc',
             '3' : 'def',
             '4' : 'ghi',
             '5' : 'jkl',
             '6' : 'mno',
             '7' : 'pqrs',
             '8' : 'tuv',
             '9' : 'wxyz',
             }
        def helper(i, partial):
            if i == len(digits):
                return [''.join(partial)]
            combos = []
            for symbol in d[digits[i]]:
                combos += helper(i + 1, partial + [symbol])
            return combos
        return helper(0,[])


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))









