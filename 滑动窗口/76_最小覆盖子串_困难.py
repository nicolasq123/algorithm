"""
https://leetcode-cn.com/problems/minimum-window-substring/
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: target str
        :rtype: str
        例 s= "ADOBECODEBANC", t="ABC". return "BANC"
        """
        if t == "":
            return ""
        if s == "":
            return ""

        start = 0
        length = 0x7fffffff
        valid = 0
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        l = r = 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 缩小
            while valid == len(need):
                if r-l < length:
                    start = l
                    length = r-l
                c = s[l]
                l += 1
                if c in need:
                    window[c] = window[c] -1
                    if window[c] < need[c]:
                        valid -=1
            
        return s[start: start+length] if length != 0x7fffffff else ""
