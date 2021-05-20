"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) <= 1:
            return len(s)
        
        res = 1
        l = 0
        r = 0
        window = {}

        # 左闭右开好了
        while r < len(s):            
            c = s[r]
            r = r+1

            window[c] = window.get(c, 0) + 1
            if window[c] == 1:
                res = max(r-l, res)

            while window[c] > 1:
                d = s[l]
                window[d] = window[d]-1
                l += 1

        return res