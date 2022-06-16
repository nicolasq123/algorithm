""" PriorityQueue使用例子
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((1, 2))
pq.put((1, 0))
pq.put((2, 3))

while not pq.empty():
    print (pq.get())
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        lists = [i for i in lists if i]
        
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        pq = PriorityQueue()
        # while True:
        for i, item in enumerate(lists):
            if item is None:
                continue
            pq.put((item.val, i)) # 值, 索引

        # p = None
        pre = ListNode()
        p = pre
        j = 0
        while pq.qsize():
            tmp = pq.get()
            idx = tmp[1]
            item = lists[idx]

            p.next=item
            p = p.next

            lists[idx]=lists[idx].next # 移动指针
            if lists[idx]:
                pq.put((lists[idx].val, idx))

        return pre.next