"""
https://leetcode-cn.com/problems/permutations/
"""
class Solution:

    def permute(self, nums):
        res = []
        n = len(nums)
        visited = {}

        def dfs(start, path):
            if start == n:
                res.append(path)
                return
            for i in nums:
                if visited.get(i) is True:
                    continue
                visited[i] = True
                dfs(start+1, path+[i])
                visited[i] = False
        
        dfs(0, [])
        return res