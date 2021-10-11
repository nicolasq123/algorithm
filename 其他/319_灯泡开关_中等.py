class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        设第i盏灯被拨了f（i）次，共n盏
        if i == 1: f(i) = 1
        if i == 2: f(i) = 2
        if i == 3: f(i) = 2 
        if i == 4: f(i) = 3
        if i == 5: f(i) = 2
        ...
        if i == 9: f(i) = 3
        平方数会被拨奇数次，非平方数会被拨偶数次
        Sum() = sum(平方数个数) = int(sqrt(n))
        """
        import math
        return int(math.sqrt(n))
