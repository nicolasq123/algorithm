"""
https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        1. 直接中序遍历
        """
        pass
        self.count = 0
        self.res = -1
        self.inorderTraverse(root, k)
        return self.res

    def inorderTraverse(self, root, k):
        if root is None:
            return
        
        self.inorderTraverse(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return
        self.inorderTraverse(root.right, k)