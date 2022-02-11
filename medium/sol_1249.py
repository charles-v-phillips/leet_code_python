class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def is_valid(s):
            paren = []
            for c in s:
                if c == '(':
                    paren.append(c)
                elif c == ')':
                    if not paren:
                        return False
                    prev = paren.pop()
                    if prev == ')':
                        return False
            if not paren:
                return True
            return False

        return is_valid(s)

class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue

            elif c == '(':
                stack.append(i)

            elif c == ')':
                if not stack:
                    to_remove.add(i)
                else:
                    stack.pop()

        to_remove = to_remove.union(set(stack))
        sb = []
        for i, c in enumerate(s):
            if i not in to_remove:
                sb.append(c)

        return "".join(sb)






if __name__ == '__main__':
    print(Solution().minRemoveToMakeValid(s = ""))