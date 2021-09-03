class Solution:
    def superEggDrop(self, k, n):
        """
        k: k个鸡蛋 k>=1
        n: n层楼   n>=1
        实际上类似：计算查找有序数列的最差时间复杂度。
        """

        """
        1. base case: dp[1][j] = j; dp[i][1] = 1
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
        
        #print("--------0", dp)

        for i in range(2, k+1):
            for j in range(2, n+1):
                # 如果用二分法做选择, 只能保证平均复杂度是Ologn, 但是这里计算的是最坏时间复杂度
                #print("--------1", i, j, dp)
                for x in range(1, j+1):
                    # x这里是选择下一个是在哪个楼层继续搜索, x属于[1,j+1)
                    # 如果在x楼层鸡蛋破了，那么鸡蛋数量减一,且在[1,x)层楼搜索 1+dp[i-1][x-1]
                    # 如果在x楼层鸡蛋没破，那么鸡蛋数量不变，且在(x,j+1)层楼搜索, 1+dp[i][j-x]
                    s = max(1 + dp[i-1][x-1],1+dp[i][j-x]) #此处计算的是最坏时间复杂度
                    dp[i][j] = min(s, dp[i][j])
                    #print("--------2", i, j, x, s, dp)

        #print("--------", dp)
        return dp[-1][-1]


class Solution2:
    def superEggDrop(self, k, n):
        """
        k: k个鸡蛋 k>=1
        n: n层楼   n>=1
        实际上类似：计算查找有序数列的最差时间复杂度。
        """

        """
        1. base case: dp[1][j] = j; dp[i][1] = 1
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


if __name__ == "__main__":
    print(Solution2().superEggDrop(2, 6))


    # dp[i][0]  dp[i-1][5]
    # dp[i][1]  dp[i-1][4]
    # dp[i][2]  dp[i-1][3]
    # dp[i][3]  dp[i-1][2]
    # dp[i][4]  dp[i-1][1]
    # dp[i][5]  dp[i-1][0]