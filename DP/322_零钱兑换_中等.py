"""
https://leetcode-cn.com/problems/coin-change/

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
"""
class Solution:
    def coinChange(self, coins, amount):
        """
        1. base case: 当amount=0, res = 0
        2. 状态: coins,amount
        3. 选择: 使用、不使用该硬币
        4. 定义dp: dp[i][j]代表使用前i-1个硬币，amount=j的时候的res
        5. 状态转移方程: dp[i][j] = min(dp[i][j-coins[i-1]] + 1, dp[i-1][j]) //这次使用或者不使用该枚硬币
        """
        if amount == 0:
            return 0
        n = len(coins)
        if n == 0:
            return -1
        dp = [[0x7fffffff for _ in range(amount+1)] for _ in range(1+n)]  # n+1在外层，代表n+1行

        for i in range(1+n):
            dp[i][0] = 0 # base case
        for i in range(1, 1+n):
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0:
                    dp[i][j] = min(dp[i][j-coins[i-1]] + 1, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return -1 if dp[-1][-1] == 0x7fffffff else dp[-1][-1]

    
    def coinChange2(self, coins, amount):
        """
        因为 dp[i][j] = min(dp[i][j-coins[i-1]] + 1, dp[i-1][j])， dp[i][j]仅依赖dp[i][j-coins[i-1]]与dp[i-1][j]
        所以可以把dp[i][j] 压缩成dp[j]
        """
        if amount == 0:
            return 0
        n = len(coins)
        if n == 0:
            return -1
        dp = [0x7fffffff for _ in range(amount+1)] 
        dp[0] = 0 # base case

        for i in range(1, 1+n):
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0:
                    dp[j] = min(dp[j-coins[i-1]] + 1, dp[j])
        return -1 if dp[-1] == 0x7fffffff else dp[-1]


if __name__ == "__main__":
    print(Solution().coinChange([1],1))