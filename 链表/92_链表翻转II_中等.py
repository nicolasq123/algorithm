"""
https://leetcode-cn.com/problems/reverse-linked-list-ii
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
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