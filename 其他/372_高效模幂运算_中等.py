class Solution:
    def superPow(self, a: int, b):
        """
        2^12 = 2^10 * 2^2
        1. 公式 a^(1000x+100y+10z+n) = a^n * (a^(100x+10y+z))^10
        2. 公式 (a%k)(b%k)%k = BD%k =========>>>>>>>>>> a^x %k == (a%k)^x %k
        """
        if len(b) == 0:
            return self.mypow(a, 0)
        
        if len(b) == 1:
            return self.mypow(a, b[0])
        base = 1337
        p1 = self.mypow(a, b[-1])
        p2 = self.mypow(self.superPow(a, b[0:-1]),10)
        return (p1*p2) % base


    def mypow(self, a, k):
        """
        a^k
        """
        if k == 0:
            return 1

        base = 1337
        a %= base

        if k % 2 == 1:
            return (a * self.mypow(a, k-1)) % base
        
        sub = self.mypow(a, k // 2)
        return (sub*sub) % base