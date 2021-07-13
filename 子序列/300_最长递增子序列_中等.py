"""
https://leetcode-cn.com/problems/longest-increasing-subsequence/
"""
"""
输入：nums = [0,3,1,6,2,2,7]
输出：4
解释：最长递增子序列是 [0,1,2,7]，因此长度为 4 。
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        1. base case: dp[i] = 1
        2. 状态: nums
        3. 选择: i
        4. 定义dp: dp[i]代表以i为尾的最长递增子序列的长度
        5. 状态转移方程: dp[i] = max(dp[i], dp[j]+1)
        """
        n = len(nums)
        if n <= 1:
            return n

        dp = [1 for _ in range(n)] # 每个元素都可以以自己为尾，初始长度应至少为1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)

    def lengthOfLIS2(self, nums):
        """
        O(nlogn)
        1. 如果当前数i，比堆中任何一个数都大，理所当然的新建堆；也就是前i个数的最长递增子序列长度+1
        2. 如果当前数i，不满足条件1；满足top[k-1]<pk < top[k]，那么放到k堆后，仍然有序
        """
        n = len(nums)
        top = [0] *n
        piles = 0
        for i in range(n):
            pk = nums[i]

            # [l, r]区间搜索 top[k-1]<pk < top[k]
            l = 0
            r = piles - 1  # 第一点
            l = self.left_bound(top, l, r, pk)
            if l == piles:
                piles += 1
            top[l] = pk
        
        return piles

    def left_bound(self, nums, l, r, target):
        tmp1 = l
        tmp2 = r
        while l<=r:
            m = l + (r-l) // 2 # 第二点
            if nums[m] < target:
                l = m + 1  # 第三点
            elif nums[m] > target:
                r = m - 1
            else:
                r = m - 1
        print(nums, tmp1, tmp2 ,target, l)
        return l


if __name__ == "__main__":
    print(Solution().lengthOfLIS2([10,9,2,5,3,7,101,18]))