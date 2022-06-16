# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(root.val)

class Solution2:
    """
    非迭代版本, 麻烦点
    """
    def postorderTraversal(self, root):
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if root is None:
            return
        s = [] #stack 之用
        p = root
        pre = None
        while p or s:
            # 入栈
            while p:
                s.append(p)
                p = p.left
            
            if s:
                # 出栈
                p = s.pop()
                if p.right is None or pre==p.right:
                    # 无右节点或者刚才无遍历过右节点
                    self.res.append(p.val)
                    pre = p
                    p = None
                else:
                    # 有右节点的情况
                    s.append(p)
                    p = p.right
