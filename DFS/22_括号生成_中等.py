class Solution:
    def generateParenthesis(self, n: int):
        self.res = []
        self.dfs(n, 0, 0, "")
        return self.res

    def dfs(self, n, l, r, path):
        """
        l代表目前多多少个左括号
        """
        print(path)
        if r == n:
            self.res.append(path)
            return
        
        if l == n:
            self.dfs(n, l, r+1, path + ")")
            return

        if l == r:
            self.dfs(n, l+1, r, path + "(")
        elif l >r:
            self.dfs(n, l+1, r, path + "(")
            self.dfs(n, l, r+1, path + ")")