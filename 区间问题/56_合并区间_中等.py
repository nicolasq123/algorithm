"""
https://leetcode-cn.com/problems/merge-intervals/
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]
"""

"""
1-3
 2---6
 ------8-10
          ----15--18
"""

class Solution:
    def merge(self, intervals):
        """
        画图理清思路
        重点在于下面的排序
        技巧: 被比较对象从res[-1]来取
        """
        n = len(intervals)
        if n <= 1:
            return intervals

        def cmp(item):
            return (item[0], -item[1])
        intervals.sort(key=cmp)

        res = []
        res.append(intervals[0])
        j = 1
        while j < n:
            last = res[-1]
            # 3种情况全部列出来,不写else
            if last[1] >= intervals[j][1]:
                j += 1
            elif last[1] < intervals[j][0]:
                res.append(intervals[j])
                j += 1
            elif last[1] >= intervals[j][0] and last[1] < intervals[j][1]:
                res[-1][1] = intervals[j][1]
                j += 1
            
        return res
