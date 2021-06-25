class Solution:
    def fib(self, n: int) -> int:
        if n <=0:
            return 0

        if n <=2:
            return 1
        a = 0 # 0
        b = 1 # 1
        c = 1 # 2

        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c