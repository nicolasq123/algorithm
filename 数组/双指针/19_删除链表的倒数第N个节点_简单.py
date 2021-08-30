"""
https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        倒序遍历,特别注意被删除的节点是头节点的情况,n比链表长度大的情况
        """
        self.cnt = 0
        self.p1 = None #前一个节点
        self.p2 = None #被删的节点
        self.p3 = None #后一个节点

        self.help(head, n)
        if self.p2 is None:
            return head # n比链表长
        if self.p1 is None:
            return self.p3
        
        self.p1.next = self.p3
        return head
    
    def help(self, head, n):
        if head is None:
            return
        self.help(head.next, n)
        self.cnt += 1
        if self.cnt == n-1:
            self.p3 = head
        elif self.cnt == n:
            self.p2 = head
        elif self.cnt == n+1:
            self.p1 = head
    

