class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        step = 0 
        i = 0

        def test(i, nums):
            start, end = i, i+1+nums[i] # () 开区间
            n = len(nums)
            m = start + 1
            mNum = 1 + nums[start]

            for k in range(start+1, min(end, n)):
                if k-start-1+1 + nums[k] >= mNum:
                    m = k
                    mNum = k-start-1+1 + nums[k]
            return m, mNum
        
        while i< n:
            start, end = i, i+1+nums[i] # () 开区间

            if start == n:
                break
            if end >= n:
                step +=1
                break
            if nums[i] == 0:
                return -1

            m, mNum = test(i, nums)
            i = m
            step +=1

        return step