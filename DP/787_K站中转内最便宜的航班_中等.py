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
        cities_map = {} # key: to, val: froms
        prices_map = {} # key: from-to val:price
        for f in flights:

            if f[1] in cities_map:
                cities_map.get(f[1]).append(f[0])
            else:
                cities_map[f[1]] = [f[0]]
            key = "{}:{}".format(f[0],f[1])
            prices_map[key] = min(prices_map.get(key, 0x7fffffff), f[2])
        # n cities
        print("---------", cities_map, prices_map)

        dp = [[[0x7fffffff for _ in range(n)] for _ in range(n)] for _ in range(k+1)] # 顺序 k,i,j
        #xx = [[0 for _ in range(1)] for _ in range(3)] 3行1列
        memo = {}

        def dp(k, src, dst):
            if dst == src:
                return 0
            if k == 0:
                return 0x7fffffff
            if "{}:{}:{}".format(k, src,dst) in memo:
                return memo["{}:{}:{}".format(k, src,dst)]
            res = 0x7fffffff
            froms = cities_map.get(dst, [])
            for fr in froms:
                key = "{}:{}".format(fr, dst)
                res = min(res, dp(k-1, src, fr)+prices_map.get(key, 0x7fffffff))
            memo["{}:{}:{}".format(k, src,dst)] = res
            return res
        r = dp(k+1, src, dst)
        return r if r != 0x7fffffff else -1



if __name__ == "__main__":
    print(Solution().findCheapestPrice(
        10,
        [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],
        6, 0, 7))