"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""
class Solution:
    def maxProfit(self, prices, fee):
        """        
        dp[i][0] 表示第i天, 未持有股票
        dp[i][1] 表示第i天, 持有股票
        相比股票买卖2,多了一个维度,买卖次数
        1. time = 2, 最多买k次
        """
        if len(prices) <=1:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 0
            dp[i][1] = -0x7fffffff-1

        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][1] + prices[i-1] - fee, dp[i-1][0]) # 未持有
            dp[i][1] = max(dp[i-1][0] - prices[i-1], dp[i-1][1])  # 持有
        return dp[-1][0]

if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)==8)