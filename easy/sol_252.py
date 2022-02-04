from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def intersect (i1, i2):
            if i1[0] <= i2[0] < i1[1]:
                return True
            return False


        n = len(intervals)
        intervals = sorted(intervals, key = lambda x: x[0])
        for i in range(n-1):
            i1 = intervals[i]
            i2 = intervals[i + 1]
            if intersect(i1,i2):
                return False
        return True

if __name__ == '__main__':
    print(Solution().canAttendMeetings(intervals = [[7,10],[2,4]]))

