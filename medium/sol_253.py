import collections
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])






if __name__ == '__main__':
    print(Solution().minMeetingRooms(intervals = [[7,10],[2,4]]))






