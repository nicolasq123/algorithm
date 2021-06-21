"""
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

"""

class Solution:
    """
    1. 方法一， hash存储每一个节点的所有祖先，hash存储每一个节点的子孙有多少个，然后在这些共同祖先里看看哪个辈分最低
    2. 方法二， 递归
    """
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if p == root:
            return p
        if q == root:
            return q
        l = self.findChild(root.left, p ,q) # l如果为None说明 root.left 是None
        r = self.findChild(root.right, p ,q)

        """
        1. 如果l r都为none，说明p,q 都在
        """

        if l and r:
            # 这里说明p和q分别是root的左右子孙
            return root
        return l or r