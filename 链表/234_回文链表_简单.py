"""
https://leetcode-cn.com/problems/palindrome-linked-list/
请判断一个链表是否为回文链表。
"""

class Solution(object):
    """
    O(1)空间， O(n)时间
    可以翻转后半部分，让后快慢指针比较, 这样并发条件下不友好
    """

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.h = head
        return self.traverse(head)

    def traverse(self, head):
        """
        后序遍历
        """
        if head is None:
            return True
        res = self.traverse(head.next)
        res = res and self.h.val == head.val
        if self.h:
            self.h = self.h.next
        return res