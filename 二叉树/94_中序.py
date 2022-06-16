# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)

import collections
class Solution2:
    """
    非迭代版本
    """
    def inorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return
        #stack 之用
        s = collections.deque([])
        p = root
        while p or s:
            # 入栈
            while p:
                s.append(p)
                p = p.left
            
            if s:
                # 出栈
                p = s.pop()
                self.res.append(p.val)
                p = p.right
