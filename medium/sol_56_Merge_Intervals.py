class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        rv = []
        for i in range(1,len(intervals)):
            start, end = intervals[i]
            pstart,pend = intervals[i-1]

            if pstart <= start <= pend:
                rv.append([pstart,max(end,pend)])
                intervals[i] = [pstart,pend]
            else:
                if len(rv) == 0:
                    rv.append(intervals[i-1])
                rv.append(intervals[i])

        return rv

if __name__ == '__main__':
    print(Solution().merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))