from stuff.linked_list_stuff import ListNode
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        fuck = {'(': ')','[':']','{':'}'}
        for c in s:
            if c in ['(', '{', '[']:
                d.append(c)
            else:
                if not d: return False
                p = d.pop()
                if c != fuck[p]:
                    return False

        if not d:
            return True
        return False



if __name__ == '__main__':
    print(Solution().isValid(']'))
