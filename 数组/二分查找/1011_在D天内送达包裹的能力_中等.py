"""
https://leetcode-cn.com/problems/koko-eating-bananas/

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
"""

class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        设载重能力为k，显然k属于[max(weights), sum(weights)],k==max(weights)时，len(weights)运完，k==sum(weights)时，1天运完。
        """
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = l + (r-l) // 2
            if self.canFinish(weights, days, m):
                r = m-1 # 满足需求
            else:
                l = m+1

        return l if self.canFinish(weights, days, l) else -1

    def canFinish(self, weights, days, k):
        d = 0
        w = 0
        for i in range(len(weights)):
            if w + weights[i] <= k:
                w += weights[i]
            else:
                d += 1
                if d > days:
                    return False
                w = weights[i]
        if w != 0:
            d += 1
        return d <= days
