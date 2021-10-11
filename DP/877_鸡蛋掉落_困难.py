class Solution:
    def superEggDrop(self, k, n):
        """
        k: k个鸡蛋 
        n: n层楼   
        实际上类似：计算查找有序数列的最差时间复杂度。
        """

        """
        1. base case: if K==1: return N; if N==0: return 0;
        2. 状态: k, n
        3. 选择: x层楼扔鸡蛋，鸡蛋破与不破
        4. 定义dp: dp[i][j],鸡蛋i个，j层楼的情况下，最少需要操作多少次
        5. 状态转移方程:
        """
        dp = [[100 for j in range(n+1)] for i in range(k+1)]

        # 1个鸡蛋，n层楼n次
        for j in range(1, n+1):
            dp[1][j] = j

        # n个鸡蛋，1层楼
        for i in range(1, k+1):
            dp[i][1] = 1
            dp[i][0] = 0
        dp[0][0] = 0

        for i in range(2, k+1):
            x = 1
            for j in range(2, n+1):
                while x < j and max(1 + dp[i-1][x-1],1+dp[i][j-x]) >= max(1 + dp[i-1][x],1+dp[i][j-x-1]):
                    # s的值类似于 y=(x-b)^2（可能表述不精确）
                    # y = max(1 + dp[i-1][x-1],1+dp[i][j-x])
                    x +=1
                dp[i][j] = max(1 + dp[i-1][x-1],1+dp[i][j-x]) # 此时x为最优解

        #print("--------", dp)
        return dp[-1][-1]


class Solution2:
    def superEggDrop(self, k, n):
        """
        简单dp版
        """
        memo = {}
        def dp(K, N):
            # base case
            if K == 1: return N
            if N == 0: return 0
            # 避免重复计算
            if (K, N) in memo:
                return memo[(K, N)]

            res = -0x7fffffff-1
            # 穷举所有可能的选择
            for i in range(1, N + 1):
                res = min(res, 
                        max(
                                dp(K, N - i), 
                                dp(K - 1, i - 1)
                            ) + 1
                    )
            # 记入备忘录
            memo[(K, N)] = res
            return res

        return dp(k, n)


if __name__ == "__main__":
    print(Solution2().superEggDrop(2, 6))


    # dp[i][0]  dp[i-1][5]
    # dp[i][1]  dp[i-1][4]
    # dp[i][2]  dp[i-1][3]
    # dp[i][3]  dp[i-1][2]
    # dp[i][4]  dp[i-1][1]
    # dp[i][5]  dp[i-1][0]