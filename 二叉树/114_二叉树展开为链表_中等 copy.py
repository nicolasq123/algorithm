"""
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

  1
 2
3

输出:
1
 2
  3
"""


class Solution:
    def flatten(self, root):
        """
        顺序同先序遍历
        递归处理
        """
        p1, _ = self.help(root)
        return p1

    def help(self, root):
        """
        返回的是链表的首尾指针
        left 和right 分别None的时候要特殊处理
        """
        if root is None:
            return None, None
        
        if root.left is None and root.right is None:
            return root, root

        if root.left is None:
            _, last = self.help(root.right)
            return root, last

        if root.right is None:
            l1, l2 = self.help(root.left)
            root.left = None
            root.right = l1
            return root, l2
        
        l1, l2 = self.help(root.left)
        r1, r2 = self.help(root.right)
        root.left = None
        root.right = l1
        l2.right = r1
        return root, r2