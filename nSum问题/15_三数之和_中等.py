"""
https://leetcode-cn.com/problems/3sum/
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
"""

class Solution(object):
    def threeSum(self, nums):
        return self.threeSumTarget(nums, 0)

    def threeSumTarget(self, nums, target):
        """
        sort是常规操作
        特别注意,数据结果非重复的条件,引入while循环在i,j,k的变动处循环处理
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        n = len(nums)
        i = 0
        j = 1
        k = n-1

        res = []
        while i <= n-3:
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j+=1
                elif s < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]: j+=1
                else:
                    k -=1
                    while j < k and nums[k] == nums[k+1]: k-=1
            
            i += 1
            while i <=n-3 and nums[i] == nums[i-1]:
                i += 1
            j = i+1
            k = n-1
        
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))