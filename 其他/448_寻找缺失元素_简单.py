class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        1. 原数组操作，直接+n用来标记这个idx+1的数存在
        2. x = (num-1) % n用来获取原值的idx
        """
        n = len(nums)
        for num in nums:
            x = (num-1) %n
            nums[x] += n

        res = [i+1 for i, num in enumerate(nums) if num < n]
        return res
