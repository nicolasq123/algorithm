"""
https://leetcode-cn.com/problems/binary-search/
"""
class Solution:
    def search(self, nums, target):
        """
        binarysearch
        1. 搜索区间是[0, n-1]
        2. m = l + (r-l) // 2, 此时的m>=l.
        3. 因为升序,所以 l = m+1, r = m-1.
        4. 结束时: l == r+1
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
                return m
        return -1