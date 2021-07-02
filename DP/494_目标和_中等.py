"""
https://leetcode-cn.com/problems/target-sum/
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        Sum(A) - Sum(B) = target
        Sum(A) + Sum(B) = sum(nums)
        Sum(A) = (target + sum(nums)) / 2

        """
        s = sum(nums)
        if (s + target) % 2 != 0:
            return 0
        new_target = (s + target) // 2
        return self.help(nums, new_target)

    def help(self, nums, target):
        """
        背包问题，注意，这一次nums[i]可能为0，所以base case会不同
        nums中满足： Sum(A) == target
        1. base case: 需要特别注意，因为nums[i]可能为0，所以需要排序，在处理base case时候要根据nums[i-1]==0特殊处理
        2. 状态: nums, target
        3. 选择: 是否使用当前数
        4. 定义dp: dp[i][j]代表使用前i个数，target=j的时候的res
        5. 状态转移方程: dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j] //这次使用或者不使用该元素
        """
        if sum(nums) < target:
            return 0
        n = len(nums)
        dp = [[0 for j in range(1+target)] for i in range(1+n)]
        # base case
        dp[0][0] = 1
        nums.sort()
        for i in range(1, 1+n):
            dp[i][0] = dp[i-1][0]*2 if nums[i-1] == 0 else dp[i-1][0] # 前i个数字，target==0的方法数; 当i为0时， dp[i][0] = 2^^i;

        for i in range(1, 1+n):
            for j in range(1, 1+target):
                if j-nums[i-1] >=0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().findTargetSumWays([9,7,0,3,9,8,6,5,7,6], 2))