"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
"""
class Solution:
    def maxProfit(self, prices):
        """        
        dp[i][k][0] 表示第i天, 第k次交易, 未持有股票
        dp[i][k][1] 表示第i天, 第k次交易, 持有股票
        相比股票买卖2,多了一个维度,买卖次数
        1. time = 2, 最多买k次
        """
        if len(prices) <=1:
            return 0
        n = len(prices)
        times = 2
        dp = [[[0 for _ in range(2)] for _ in range(times+1)] for _ in range(n+1)]
        
        # base case
        # dp[i][0][0] = 0          
        # dp[i][0][1] = -0x7fffffff-1 不可能持有股票
        # dp[-1][k][0] = 0
        # dp[-1][k][1] = -0x7fffffff-1
        for i in range(n+1):
            dp[i][0][0] = 0
            dp[i][0][1] = -0x7fffffff-1
        
        for k in range(times+1):
            dp[0][k][0] = 0
            dp[0][k][1] = -0x7fffffff-1

        for i in range(1, n+1):
            for k in range(1, times+1):
                dp[i][k][0] = max(dp[i-1][k][1] + prices[i-1], dp[i-1][k][0]) # 未持有
                dp[i][k][1] = max(dp[i-1][k-1][0] - prices[i-1], dp[i-1][k][1])  # 持有
        return dp[-1][-1][0]

if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5]))