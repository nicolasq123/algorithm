"""
https://leetcode-cn.com/problems/minimum-falling-path-sum/
"""
class Solution:
    def minFallingPathSum(self, matrix):
        """
        1. base case:
        2. 状态: row
        3. 选择: 左下，直下，右下
        4. 定义dp:
        5. 状态转移方程: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])
        """
        n = len(matrix)
        if n == 0:
            return 0
        if n == 1:
            return matrix[0][0]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j] # base case

        for i in range(1,n):
            for j in range(n):
                dp[i][j] = dp[i-1][j]
                if j-1 >=0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                if j+1 <n:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])
                dp[i][j] = dp[i][j] + matrix[i][j]

        res = dp[-1][0]
        for j in range(1, n):
            res = min(res, dp[-1][j])
        print(dp)
        return res


if __name__ == "__main__":
    print(Solution().minFallingPathSum([[17,82],[1,-44]]))