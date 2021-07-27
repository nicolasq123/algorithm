"""
https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/
"""

class Solution:
    def longestPalindromeSubseq(self, s):
        """
        1. base case: 
        2. 状态: s
        3. 选择: 
        4. 定义dp: dp[i][j]代表s[i,j+1] 的最大回文子序列长度
        5. 状态转移方程: 
        """
        n = len(s)
        # dp 数组全部初始化为 0
        dp = [[0 for j in range(n)] for i in range(n)]
        # base case
        for i in range(n):
            dp[i][i] = 1
        # 反着遍历保证正确的状态转移
        i = n-1
        while i >=0:
            j = i+1
            while j <n:
                # 因为dp[i][j]的依赖关系，所以这样遍历
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                j += 1
            i -= 1
        # 整个 s 的最长回文子串长度
        return dp[0][n - 1]