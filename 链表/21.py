# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        p1 = list1
        p2 = list2
        p = None
        if p1.val<p2.val:
            p = p1
            p1=p1.next
        else:
            p = p2
            p2=p2.next
        
        tmp = p

        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    tmp.next = p1
                    p1 = p1.next
                else:
                    tmp.next = p2
                    p2 = p2.next
                
                tmp = tmp.next
                continue
            
            if p1:
                tmp.next = p1
                break

            if p2:
                tmp.next = p2
                break
        
        return p