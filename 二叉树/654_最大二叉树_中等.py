"""
https://leetcode-cn.com/problems/maximum-binary-tree/
给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

二叉树的根是数组 nums 中的最大元素。
左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        m = self.findMax(nums)

        root = TreeNode(nums[m])
        root.left = self.constructMaximumBinaryTree(nums[:m])
        root.right = self.constructMaximumBinaryTree(nums[m+1:])
        return root

    def findMax(self, nums):
        res = 0
        m = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= m:
                res = i
                m = nums[i]
        return res