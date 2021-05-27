"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
"""

class Solution:
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        """
        先找到[left,right],断开链表,反转,连接上
        """
        i = 0
        

    
    def reverse(self, head):
        if head is None:
            return None
        
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

    