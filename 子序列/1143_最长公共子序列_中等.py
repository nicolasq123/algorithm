"""
https://leetcode-cn.com/problems/longest-common-subsequence/
"""

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str):
        """
        1. base case:
        2. 状态: s1, s2
        3. 选择: i, j
        4. 定义dp: dp[i][j]代表以s1[:i],s2[:j]的最长公共子序列
        5. 状态转移方程: 
        """
        n1 = len(s1)
        n2 = len(s2)
        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):                
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

