class Solution:
    def trailingZeroes(self, n):

        div = 5
        res = 0
        while n >= div:
            res +=  n // div
            div *= 5
        return res
    
    def preimageSizeFZF(self, k):
        r = self.right_bound(k)
        l = self.left_bound(k)
        if r == -1 or l == -1:
            return 0
        return r - l +1
    
    def left_bound(self, k):
        l = 0
        r = k*5 + 5
        # 搜索空间[l,r]
        while l <= r:
            m = l + (r-l)//2
            s = self.trailingZeroes(m)
            if s == k:
                r = m -1
            elif s > k:
                r = m -1
            elif s < k:
                l = m +1
        return l if self.trailingZeroes(l) == k else -1
    
    def right_bound(self, k):
        l = 0
        r = k*5 + 5
        # 搜索空间[l,r]
        while l <= r:
            m = l + (r-l)//2
            s = self.trailingZeroes(m)
            if s == k:
                l = m +1
            elif s > k:
                r = m -1
            elif s < k:
                l = m +1
        return r if self.trailingZeroes(r) == k else -1

# 二分查找左边界
# def left_bound(nums, target):
#     l = 0
#     r = len(nums)-1
#     # 搜索空间[l,r]
#     while l <= r:
#         m = l + (r-l)//2
#         print(l,r,m)
#         if nums[m] == target:
#             r = m -1
#         elif nums[m] > target:
#             r = m -1
#         elif nums[m] < target:
#             l = m +1
#     if l < len(nums) and nums[l] == target:
#         return l
#     return -1

if __name__ == '__main__':
    print(Solution().preimageSizeFZF(5))