class Solution:

    def isMatch(self, s: str, p: str):
        """
        1. base case:
        2. 状态: i,j
        3. 选择: j+1 == *时，匹配or不匹配
        4. 定义dp: dp[i][j] 为 s[0:i] 能不能被 p[0:j]匹配.
        5. 状态转移方程:
        """
        n1 = len(s)
        n2 = len(p)

        dp = [[False for j in range(1+n2)] for i in range(1+n1)]
        dp[0][0] = True

        def isEq(i, j):
            if i == 0:
                return False
            return p[j-1] in  [s[i-1], '.']

        for i in range(0, 1+n1):
            for j in range(1, 1+n2):
                if p[j-1] == '*': #当前为#,合法说明j>1,不会溢出
                    # i = 3， j = 3  aaa aa*
                    # dp[i][j-2] 代表 aaa和a匹配，也就是说"a*"不匹配字符。 
                    # isEq(i, j-1): s[3-1] == s[3-1-1]
                    # dp[i-1][j] 代表 aa 和 aa*匹配
                    # or 后面的表达式实际上是往前推的
                    dp[i][j] = dp[i][j-2] or (isEq(i, j-1) and dp[i-1][j])
                else:
                    dp[i][j] = isEq(i,j) and dp[i-1][j-1]

        return dp[-1][-1]

if __name__ == "__main__":
    print(Solution().isMatch("aa", "a*a"))
