"""
https://leetcode-cn.com/problems/invert-binary-tree/
翻转一棵二叉树。

     4
   /   \
  2     7
 / \   / \
1   3 6   9

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root