"""
https://leetcode-cn.com/problems/n-queens/
"""

class Solution:
    """
    1. DFS代码
    2. valid函数的判断用三个dict来加速搜索
    """
    def solveNQueens(self, n):
        res = []
        visited_col = {}
        visited_k = {}
        visited_k_neg = {}

        def dfs(row, path):
            if row == n:
                res.append(path)
                return
            for i in range(n):
                x = row
                y = i
                if not self.valid(visited_col, visited_k, visited_k_neg, x, y):
                    continue

                visited_col[y] = True
                visited_k[y-x] = True
                visited_k_neg[y+x] = True

                dfs(row+1, path+[self.gen_str(i,n)])

                visited_col[y] = False
                visited_k[y-x] = False
                visited_k_neg[y+x] = False

        dfs(0, [])
        return res

    def gen_str(self, i, n):
        return "."*(i)+ "Q" + "."*(n-i-1)

    def valid(self, visited_col, visited_k, visited_k_neg, x, y):
        """
        斜线公式: y = kx + b
        1. k = 1时, b 属于[1-n, n-1]
        2. k = -1时, b 属于[0, 2n-2]

        visited_col: 列
        visited_k: k=1时的b的值代表的直线
        visited_k_neg: k=-1时的b的值代表的直线
        """
        if visited_col.get(y):
            return False
        if visited_k.get(y-x):
            return False
        if visited_k_neg.get(y+x):
            return False

        return True


if __name__ == "__main__":
    print(Solution().solveNQueens(4))