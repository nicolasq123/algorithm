"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        l = 0
        p = head
        while p:
            l += 1
            p = p.next

        for i in range(l // k):
            left = 1 + k*i
            right = k*(i+1)
            head = self.reverseBetween(head, left, right)
        return head

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        prel, l = self.findNode(head, left)
        r, postr = self.findNode(head, right+1)

        r.next = None

        new_head = self.reverse(l)

        l.next = postr
        if prel:
            prel.next = new_head
        if left == 1:
            return new_head
        return head

    
    def findNode(self, head, target):
        pre = None
        p = head
        n = 1
        while p:
            if n == target:
                return pre,p
            n += 1
            pre = p
            p = p.next
        return pre, p


    def reverse(self, head):
        if head is None:
            return head
        
        p1 = None
        p2 = head
        p3 = head.next

        while p2:
            p2.next = p1

            p1 = p2
            p2 = p3
            if p3:
                p3 = p3.next
        return p1