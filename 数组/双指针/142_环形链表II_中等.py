"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        设S1为初始点点与所求点的距离
        设S2为快慢指针第一次相遇的点与所求点的距离
        S1 + S2 +N * circle = 2*(S1 + S2) => S1+S2 = N*Circle 
        1. 先让快慢指针走，在某点相遇
        2. 然后快指针从head开始，并且速度都是1步/次
        3. 这一次相遇的点就是环起始点
        """
        slow = head
        fast = head
        # 第一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None # 无环
        
        # 第二步
        fast = head
        while fast:
            # 要注意先判断，防止目标节点是head
            if slow == fast:
                break
            fast = fast.next
            slow = slow.next
        return fast