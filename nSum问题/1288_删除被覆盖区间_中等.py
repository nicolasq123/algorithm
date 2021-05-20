"""
https://leetcode-cn.com/problems/remove-covered-intervals/
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
在完成所有删除操作后，请你返回列表中剩余区间的数目。

输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
"""

class Solution:
    def removeCoveredIntervals(self, intervals):
        """
        画图理清思路
        重点在于下面的排序
        """
        n = len(intervals)
        if n <= 1:
            return n
        
        def cmp(item):
            return (item[0], -item[1])
        intervals.sort(key=cmp)
        
        res = 0
        i = 0
        j = 0
        while i < n:
            res += 1
            j = i+1
            while j < n and intervals[i][1] >= intervals[j][1]:
                j += 1
            i = j
        return res

