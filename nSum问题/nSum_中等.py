class Solution(object):
    def nSum(self, nums, n, start, target):
        """
        扩展,可以尝试先写2Sum,然后找规律递归就行了
        """
        if n < 2 or len(nums) < n:
            return []

        nums.sort()
        if n == 2:
            return self.twoSum(nums, start, target)

        i = start
        res = []
        while i < len(nums):
            tmp = self.nSum(nums, n-1, i+1, target-nums[i])
            #print("----", nums, n-1, i+1, target-nums[i], tmp)
            for t in tmp:
                res.append(t+[nums[i]])
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]: i += 1     
        return res

    def twoSum(self, nums, start, target):
        # nums.sort()
        i = start
        j = len(nums)-1
        res = []
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                res.append([nums[i], nums[j]])
                i += 1
                while nums[i] == nums[i-1] and i < j:
                    i += 1
            elif s < target:
                i += 1
                while nums[i] == nums[i-1] and i < j:
                    i += 1
            else:
                j -= 1
                while nums[j] == nums[j+1] and i < j:
                    j -=1
        return res


if __name__ == '__main__':
    # [[-1,-1,2],[-1,0,1]]
    print(Solution().nSum([-1,0,1,2,-1,-4], 3, 0, 0))


    #print(Solution().nSum([2,7,11,15], 2, 0, 18))