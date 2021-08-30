class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        1. end顺序，start逆序。 所以intervals[n+1][1] >= intervals[n][1].
        """
    
        def cmp(item):
            return (item[1], -item[0])
        intervals.sort(key=cmp)
        res = 0

        start = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[start][1]:
                res += 1
            else:
                start = i
        return res
