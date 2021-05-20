"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""
class Solution:
    def maxProfit(self, prices):
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
            dp[i][0] = max(dp[i-1][1] + prices[i-1], dp[i-1][0]) # 未持有
            if i >= 2:
                dp[i][1] = max(dp[i-2][0] - prices[i-1], dp[i-1][1])  # 持有
            else:
                dp[i][1] = max( - prices[i-1], dp[i-1][1])
        return dp[-1][0]

if __name__ == '__main__':
    print(Solution().maxProfit([1,2,3,4,5]))