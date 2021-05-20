"""
https://leetcode-cn.com/problems/permutation-in-string/
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        if s1 == "":
            return True
        if s2 == "":
            return False

        l = 0
        r = 0

        valid = 0
        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        # 左闭右开好了
        while r < len(s2):
            c = s2[r]
            r = r+1
            if c not in need:
                l = r
                window = {}
                valid = 0
                continue

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 缩小
            while r-l >= len(s1):
                if valid == len(need):
                    return True

                c = s2[l]
                l = l+1
                if c in need:
                    if window[c] == need.get(c):
                        valid -=1                    
                    window[c] = window[c] - 1

        return False