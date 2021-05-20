"""
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
"""
class Solution(object):
    def findAnagrams(self, s, t):
        """
        :type s: str
        :type t: str
        """
        res = []

        if t == "":
            return res
        if s == "":
            return res

        l = 0
        r = 0

        valid = 0
        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        while r < len(s):
            c = s[r]
            r = r+1
            if c not in need:
                l = r
                valid = 0
                window = {}
                continue

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            # 缩小
            while valid == len(need):
                if r-l == len(t) and valid == len(need):
                    res.append(l)
                c = s[l]
                l = l+1
                if c in need:
                    window[c] = window[c] - 1
                    if window[c] < need.get(c, 0):
                        valid -= 1

        return res