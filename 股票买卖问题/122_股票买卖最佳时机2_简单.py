"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
"""
class Solution:
    def maxProfit(self, prices):
        """
        dp[i][0] 表示第i天未持有股票
        dp[i][1] 表示第i天持有股票
        空间可以压缩到O(1)
        """
        if len(prices) <=1:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for i in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            
        return dp[-1][0]

if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))