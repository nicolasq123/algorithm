"""
https://leetcode-cn.com/problems/split-array-largest-sum/

输入：nums = [7,2,5,10,8], m = 2
输出：18
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        """
        方法一,显然，n=len(nums),分割方式有C(n-1,m-1)种, 暴力算法
        方法二,k属于[sum(nums)//m, sum(nums) - m-1个最小的值], 二分查找.时间复杂度O(n) * O(log(r-l))
        """
        l = sum(nums) // m
        r = self.getMax(nums, m) # 上界也可以用sum(nums)，慢一点

        while l <= r:
            mid = l + (r - l) // 2
            print(l, r, mid)
            if self.canFinish(nums, m, mid):
                r = mid-1
            else:
                l = mid+1
        print(l, self.canFinish(nums, m, l))
        if self.canFinish(nums, m, l):
            return self.canFinishMaxVal(nums, m, l)
        return -1
    
    def canFinishMaxVal(self, nums, m, k):
        # 获取能够分割的连续子数组max(sum(子数组))
        res = 0
        val = 0
        for i in range(len(nums)):
            if val + nums[i] <=k:
                val += nums[i]
                continue
            res = max(res, val)
            val = nums[i]
        
        res = max(res, val)
        return res
    
    def canFinish(self, nums, m, k):
        # 分割的时候，连续子数组和<=k值
        part = 0
        val = 0
        for i in range(len(nums)):
            if val + nums[i] <=k:
                val += nums[i]
                continue

            part += 1
            if part >m:
                return False
            val = nums[i]
        
        if val:
            part += 1
        return part <=m


    def getMax(self, nums, m):
        n = len(nums)
        return max(sum(nums[m:]), sum(nums[:n-m+1]))

if __name__ == "__main__":
    print(Solution().splitArray([7,2,5,10,8], 2))