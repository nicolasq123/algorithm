"""
https://leetcode-cn.com/problems/edit-distance/
"""
"""
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""
class Solution:
    def minDistance(self, word1, word2):
        """
        1. base case: n1 == 0 or n2 == 0； return n1+n2
        2. 状态: word1, word2
        3. 选择: 插入/变换/删除
        4. 定义dp: dp[i][j]代表word1[:i] 变成word2[:j]的时候，最少有多少种操作
        5. 状态转移方程: dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1) # 如果字符不相同的话
        """
        n1 = len(word1)
        n2 = len(word2)
        if n1 == 0 or n2 == 0:
            return n1 + n2

        dp = [[0 for _ in range(1+n2)] for _ in range(1+n1)]
        # base case
        for i in range(1+n1):
            dp[i][0] = i
        for j in range(1+n2):
            dp[0][j] = j

        for i in range(1, 1+n1):
            for j in range(1, 1+n2):
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().minDistance("horse", "ros"))