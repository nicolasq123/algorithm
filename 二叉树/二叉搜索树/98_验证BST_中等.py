"""
https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.help(root, None, None)

    def help(self, root, min, max):
        if root is None:
            return True
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return self.help(root.left, min, root) and self.help(root.right, root, max)