class Solution:
    def trailingZeroes(self, n):

        div = 5
        res = 0
        while n >= div:
            res +=  n // div
            div *= 5
        return res