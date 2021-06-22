"""
https://leetcode-cn.com/problems/split-array-largest-sum/

输入：nums = [7,2,5,10,8], m = 2
输出：18
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        """
        方法一,显然，n=len(nums),分割方式有C(n-1,m-1)种, 暴力算法可以把这些都计算出来？
        方法二,k属于[sum(nums)//m, sum(nums) - m-1个最小的值], 二分
        """
        l = sum(nums) // m
    

    def getMax(self, nums, m):
        s = sum(nums)
        







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
