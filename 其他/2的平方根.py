"""
1. 2的平方根
2. 要求精确到小数点后10位
"""
class Solution:
    def sqrt(self):
        """
        1. 二分法.
        2. 牛顿迭代法： x(n+1) = x(n) - f(xn)/f'(xn) (收敛速度更快)
        """
        l = 1+0.0000000001
        r = 2-0.0000000001
        while l <= r:
            m = round((l+r) / 2, 10)
            if self.equalTwo(m):
                return m
            if m*m > 2:
                r = m-0.0000000001
            elif m*m < 2:
                l = m+0.0000000001
        return -1

    def equalTwo(self, x):
        """
        比较x^2 和2是否相等(精确到小数点后10位),应满足
        1. x^2 < 2
        2. (x+0.0000000001)^2 > 2
        """
        return x*x < 2 and (x+0.0000000001)*(x+0.0000000001) > 2
    
    def sqrt2(self):
        """
        f(xn) = x^2 -2
        牛顿迭代法, x(n+1) = x(n) - f(xn)/f'(xn) = x(n) - (xn^2-2)/2Xn
        """
        x = 1
        while not self.equalTwo(x):
            print("------------", x)
            x = x-(x*x-2)/2/x
        return x

if __name__ == "__main__":
    import math
    print(round(math.sqrt(2), 10), Solution().sqrt2())