from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        1. base case: src
        2. 状态: k, cities
        3. 选择: 向其他城市走，不走回头路
        4. 定义dp: dp[i][j],为from i to j的最小price
        5. 状态转移方程: dp[i][j]= min E (dp[i][m]+dp[m][j])
        """
        cities_map = {} # key: from, val: tos
        prices_map = {} # key: from-to val:price
        for f in flights:
            
            if f[0] in cities_map:
                cities_map.get(f[0]).append(f[1])
            else:
                cities_map[f[0]] = [f[1]]
            key = "{}:{}".format(f[0],f[1])
            prices_map[key] = min(prices_map.get(key, 0x7fffffff), f[2])
        # n cities
        print("---------", cities_map, prices_map)

        dp = [[[0x7fffffff for _ in range(n)] for _ in range(n)] for _ in range(k+1)] # 顺序 k,i,j
        #xx = [[0 for _ in range(1)] for _ in range(3)] 3行1列
        
        # base case
        for i in range(n):
            for j in range(n):
                if i == j:
                    for x in range(k+1):
                        dp[x][i][j] = 0
                else:
                    key = "{}:{}".format(i, j)
                    dp[0][i][j] = prices_map.get(key, 0x7fffffff)
        print("---------", dp)


        for x in range(1, k+1):
            for i in range(n):
                for j in range(n):
                    tos = cities_map.get(i, [])
                    if not tos:
                        continue
                    for t in tos:
                        dp[x][i][j] = min(dp[x-1][i][t]+dp[0][t][j], dp[x][i][j]) #只依赖dp[x-1]的
        print("---------", dp)
        return dp[k][src][dst] if dp[k][src][dst] != 0x7fffffff else -1


if __name__ == "__main__":
    print(Solution().findCheapestPrice(
        10,
        [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],
        6, 0, 7))