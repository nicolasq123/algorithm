"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

     4
   /   \
  2     7
 / \   / \
1   3 6   9
"""

class Node:
    def __init__(self, val= 0, left= None, right= None, next= None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections
class Solution(object):
    def connect(self, root):
        """
        两种方法: BFS、递归亦可
        """
        if root is None:
            return
        q = collections.deque([])
        q.append(root)
        while len(q):
            l = len(q)
            tmp = None
            for i in range(l):
                item = q.popleft() # 注意是popleft,因为要用到队列的功能,且q是deque,不能写成pop了
                # 处理特殊逻辑
                if i != 0:
                    tmp.next = item
                tmp = item
                # 添加元素
                if item.left: q.append(item.left)
                if item.right: q.append(item.right)
        return root
