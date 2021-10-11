class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        差分数组, O(n)的时间
        10     -10
           +20    -20
                  
           +25           -25

        10 55  45  25  25  0
        """
        diff = [0 for _ in range(n+1)]
        for b in bookings:
            first = b[0] - 1
            second = b[1]
            v = b[2]
            diff[first] += v
            diff[second] -= v
        
        res = [0 for _ in range(n)]
        for i in range(n):
            if i ==0:
                res[i] = diff[i]
                continue
            res[i] = diff[i]+res[i-1]
        return res
        
        