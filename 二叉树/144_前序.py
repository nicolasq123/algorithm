# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return

        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

class Solution2:
    """
    非迭代版本
    """
    def preorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return
        s = [] #stack 之用
        p = root
        while p or s:
            # 入栈
            while p:
                self.res.append(p.val)
                s.append(p)
                p = p.left
            
            if s:
                # 出栈
                p = s.pop()
                p = p.right
