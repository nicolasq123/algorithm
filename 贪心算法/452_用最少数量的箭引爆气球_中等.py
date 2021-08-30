class Solution:
    def findMinArrowShots(self, points):
        """
        1. end顺序，start逆序。 points[n+1][1] >= points[n][1].
        """
    
        def cmp(item):
            return (item[1], -item[0])
        points.sort(key=cmp)
        res = 0

        start = 0
        for i in range(1, len(points)):
            if points[i][0] <= points[start][1]:
                res += 1
            else:
                start = i
        return len(points)-res
