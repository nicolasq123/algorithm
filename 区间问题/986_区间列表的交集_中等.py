"""
https://leetcode-cn.com/problems/interval-list-intersections/
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
返回这 两个区间列表的交集 。
形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        画图理清思路
        """
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        i = 0
        j = 0
        m = len(firstList)
        n = len(secondList)
        res = []
        while i <m and j <n:
            if firstList[i][0] < secondList[j][0]:
                small = firstList[i]
                big   = secondList[j]
            else:
                big  = firstList[i]
                small   = secondList[j]

            if small[1] < big[0]:
                pass
            elif small[1] >= big[0] and small[1] <= big[1]:
                res.append([big[0], small[1]])
            else:
                res.append(big)

            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1

        return res


