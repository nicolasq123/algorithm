"""
https://leetcode-cn.com/problems/partition-equal-subset-sum/
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
"""

class Solution:
    def canPartition(self, nums):
        """
        1. SumA = SumB = 1/2 * SumALL
        2. 问题退化成Sum(C) = target = 1/2 * SumALL , C是一个子集
        """
        s = sum(nums)
        if s // 2 * 2 != s:
            return False
        return self.findTarget(nums, s//2)

    
    def findTarget(self, nums, target):
        """
        DP
        [1,5,11,5] 里寻找和为11的子集
        dp[i][j] = x 表示，对于前 i 个物品，当前背包的容量为 j 时，若 x 为 true，则说明可以恰好将背包装满
        """
        if target == 0:
            return True
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True # base case

        for i in range(n):
            for j in range(1, target+1):
                if j-nums[i] >=0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]