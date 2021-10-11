class Solution:
    def maxCoins(self, nums):
        """
         [3,1,5,8] ->
        1. base case: n = 0, 1,2
        2. 状态: 
        3. 选择: 
        4. 定义dp: 
        5. 状态转移方程: dp[i][j] 代表戳破开区间(i,j)的元素
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        new_nums = [1] + nums + [1]
        for i in range(n, -1, -1):
            for j in range(i+1, n+2, 1):
                for k in range(i+1, j):
                    # i<k<j, dp[i][j]依赖dp[i][k]+dp[k][j]
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+new_nums[i]*new_nums[j]*new_nums[k])
        return dp[0][n+1]


if __name__ == "__main__":
    print(Solution().maxCoins([3,1,5,8]))

