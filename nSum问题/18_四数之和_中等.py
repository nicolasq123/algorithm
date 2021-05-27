"""
https://leetcode-cn.com/problems/4sum/
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：答案中不可以包含重复的四元组。

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        注意边界条件
        """
        if len(nums) < 4:
            return []
        nums.sort()

        p1 = 0
        res = []
        while p1 <= len(nums)-4:
            tmp = self.threeSumTarget(nums[p1+1:], target-nums[p1])
            print("-------", nums[p1:], target-nums[p1], tmp)
            for t in tmp:
                res.append([nums[p1]]+t)
            p1 += 1
            while p1 <= len(nums)-4 and nums[p1] == nums[p1-1]: p1 += 1

        return res


    def threeSumTarget(self, nums, target):
        """
        sort是常规操作
        特别注意,数据结果非重复的条件,引入while循环在i,j,k的变动处循环处理
        """
        if len(nums) < 3:
            return []
        
        # nums.sort()
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
    print(Solution().fourSum([1,0,-1,0,-2,2], 0))