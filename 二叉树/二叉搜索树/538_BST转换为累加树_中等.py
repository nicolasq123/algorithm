"""
https://leetcode-cn.com/problems/convert-bst-to-greater-tree/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        遍历right，root，left
        1. 方法一: 用last存储上一次遍历的值
        2. 方法二: 用sum存储累加值
        """
        self.last = None
        self.sum = 0
        self.traverse1(root)
        #self.traverse2(root)
        return root

    def traverse1(self, root):
        if root is None:
            return

        self.traverse1(root.right)
        # 这里实际上加的是上一个遍历的节点值
        if self.last:
            root.val += self.last.val
        self.last = root
        self.traverse1(root.left)
    
    def traverse2(self, root):
        if root is None:
            return

        self.traverse2(root.right)
        # 这里实际上加的是上一个遍历的节点值
        self.sum += root.val
        root.val = self.sum
        self.traverse2(root.left)
