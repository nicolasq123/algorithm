class Solution:
    """
    4122
    12 4
    """
    def findErrorNums(self, nums):
        n = len(nums)
        for i, num in enumerate(nums):
            idx = (num - 1) % n
            nums[idx] += n
        
        mis = -1
        dup = -1
        for i, num in enumerate(nums):
            if num // n > 1:
                dup = i+1
            if nums < n:
                mis = i+1
        return [dup, mis]