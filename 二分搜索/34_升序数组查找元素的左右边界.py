"""
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
class Solution:
    def searchRange(self, nums, target):
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
    
    def left_bound(self, nums, target):
        l = 0
        r = len(nums) - 1  # 第一点
        while l<=r:
            m = l + (r-l) // 2 # 第二点
            if nums[m] < target:
                l = m + 1  # 第三点
            elif nums[m] > target:
                r = m - 1
            else:
                r = m - 1
        # 注意越界情况
        if l >= len(nums) or nums[l] != target:
            return -1

        return l

    def right_bound(self, nums, target):
        """
        算法含义: 比target大的个数
        """
        l = 0
        r = len(nums) - 1  # 第一点
        while l<=r:
            m = l + (r-l) // 2 # 第二点
            if nums[m] < target:
                l = m + 1  # 第三点
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1 # 如果l = m, 会死循环
        # 注意越界情况
        if r < 0 or nums[r] != target:
            return -1
        return r