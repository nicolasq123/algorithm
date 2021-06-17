"""
https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    核心思想：
    1. isBST 会判断
    2. 后续遍历存储值，当然这里可以省略
    """
    def __init__(self):
        self.res = 0

    def maxSumBST(self, root):
        self.isBST(root)
        return self.res
    
    def isBST(self, root):
        """
        返回 子树Sum值,子树最小值，最大值，是否BST
        """
        if root is None:
            return 0, 0, 0, True
        
        mi = root.val
        ma = root.val
        res = True
        l = 0
        r = 0
        if root.left:
            l, miT, maT, bT = self.isBST(root.left)
            res = res and bT and root.val > maT
            mi = min(mi, miT)
            ma = max(ma, maT)

        if root.right:
            r, miT, maT, bT = self.isBST(root.right)
            res = res and bT and root.val < miT
            mi = min(mi, miT)
            ma = max(ma, maT)

        if res:
            self.res = max(self.res, l + r + root.val)
        return l + r + root.val, mi, ma, res
