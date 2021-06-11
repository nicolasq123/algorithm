# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])

        idx = self.findIdx(inorder, postorder[-1])

        # left
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.left = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        
        return root
        

    def findIdx(self, nums, target):
        for i, v in enumerate(nums):
            if v == target:
                return i
        return -1