class Solution:
    def findKthLargest(self, nums, k):
        """
        1. 快排，O（N）
        """
        if k >len(nums):
            return min(nums)
        
        l = 0
        r = len(nums)-1
        k = len(nums)-k
        # 左闭右闭
        while l<=r:
            p = self.partition(nums, l ,r)
            if p == k:
                return nums[k]
            if p < k:
                l = p +1
            else:
                r = p -1
        return -1

    def fastSort(self, nums):
        self.fastSortHelp(nums, 0, len(nums)-1)
        return nums

    def fastSortHelp(self, nums, l, r):
        # 双闭
        if l >= r:
            return
        p = self.partition(nums, l, r)
        self.fastSortHelp(nums, l, p-1)
        self.fastSortHelp(nums, p+1, r)

    def partition(self, nums, l, r):
        if l == r:
            return l # only 1 element
        pivot = nums[l]
        i = l + 1
        j = r
        # 左闭右闭
        while True:
            print("x----", i, j, l, r, pivot, nums, nums[i])
            while nums[i] <= pivot:
                if i == r:
                    break
                i += 1
                #print("----", i, j, l, r, pivot, nums)

            while nums[j] > pivot:
                if j == l:
                    break
                j -= 1

            if i >= j:
                break
            self.swap(nums, i, j)
        self.swap(nums, j, l)
        return j
    
    def swap(self, nums, l, r):
        nums[l], nums[r] = nums[r], nums[l]

if __name__ == "__main__":
    #print(Solution().fastSort([1,4,2]))
    print(Solution().findKthLargest([3,3,3,3,3,3,3,3], 1))