"""
https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/
"""

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        1. base case:
        2. 状态: s1, s2
        3. 选择: 删s1，删s2
        4. 定义dp: dp[i][j]代表以s1[:i],s2[:j]的minDistance
        5. 状态转移方程: 
        """
        n1 = len(s1)
        n2 = len(s2)

        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        dp[0][0] = 0 # base case
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for i in range(1, n1+1):
            for j in range(1, n2+1):                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1]+ ord(s2[j-1]))
        return dp[-1][-1]

