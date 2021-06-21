"""
https://leetcode-cn.com/problems/count-complete-tree-nodes/

"""

class Solution(object):
    def __init__(self):
        self.memo_l = {} # 这里可以存储多个节点的hl加快计算
        self.memo_r = {}

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        l = r = root
        hl = hr = 0
        while l:
            l = l.left
            hl +=1
        while r:
            r = r.right
            hr +=1
        
        if hl == hr:
            return pow(2, hl) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)