from typing import List
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        for i in range(len(ppid)):
            if ppid[i] == kill:
                print(i)
                break


if __name__ == '__main__':
    Solution().killProcess(pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5)
