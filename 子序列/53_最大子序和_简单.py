"""
https://leetcode-cn.com/problems/maximum-subarray/
"""
"""
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1. base case: dp[0] = nums[0]
        2. 状态: nums
        3. 选择: i
        4. 定义dp: dp[i]代表以i为尾的最大子序和
        5. 状态转移方程: dp[i] = max(dp[i-1] + nums[i], nums[i])
        """
        if len(nums) == 0:
            return 0
        
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        n = len(nums)
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
        
        