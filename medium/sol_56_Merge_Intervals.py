class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        rv = []
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            pstart, pend = intervals[i-1]

            if start <= pstart <= end:
                interval = [pstart]


if __name__ == '__main__':
    print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))