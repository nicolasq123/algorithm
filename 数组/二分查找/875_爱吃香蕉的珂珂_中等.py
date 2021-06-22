"""
https://leetcode-cn.com/problems/koko-eating-bananas/

输入: piles = [3,6,7,11], H = 8
输出: 4
"""
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        """
        设每小时吃k个香蕉，显然，k属于[1, max(piles)],k==max(piles)时，len(piles)可以吃完，k==1时，sum(piles)可以吃完。
        公式 sum(ceil(piles[i] / k)) <= h
        方法： 在[1, max(piles)]区间，二分查找left bound
        """
        if h < len(piles):
            return -1 # todo

        low = 1
        hight = max(piles)
        while low <= hight:
            m = low + (hight - low) // 2
            if self.canFinish(piles, m, h):
                hight = m-1 # 符合条件
            else:
                low = m+1 # 不符条件

        return low if self.cal(piles, low, h) else -1


    def canFinish(self, piles, k, h):
        s = 0
        for p in piles:
            s += self.ceil(p, k)
        return s <= h

    def ceil(self, i, j):
        if j <= 0:
            return -1 # todo
        if i // j * j== i:
            return i // j
        return (i // j) + 1
