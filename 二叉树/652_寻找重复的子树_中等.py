# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        """
        用str post
        """
        self.post_dict = {}
        
        self.res = {}
        self.postOrder(root)
        return [k for k,_ in self.res.items()]

    def postOrder(self, root):
        if root is None:
            return '#'
        l = self.postOrder(root.left)
        r = self.postOrder(root.right)
        s = l + ',' + r + ',' + str(root.val)

        if self.post_dict.get(s):
            self.res[self.post_dict.get(s)] = True # 记录结果，防止重复
        else:
            self.post_dict[s] = root

        return s
