"""
https://leetcode-cn.com/problems/russian-doll-envelopes/
"""
"""
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
"""

class Solution:
    def maxEnvelopes(self, envelopes):
        nums = envelopes
        nums.sort(key=lambda x: (x[0], -x[1]))
        tmps = [r[1] for r in nums]
        # 这里就转化为最长递增子序列长度
        print("---1", nums, tmps)
        return self.lengthOfLIS2(tmps)

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
    print(Solution().maxEnvelopes([[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]))