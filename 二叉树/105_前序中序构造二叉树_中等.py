class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # 找到root

        root = TreeNode(preorder[0])
        idx = self.findIdx(inorder, preorder[0])

        # left
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root
    
    def findIdx(self, nums, target):
        for i, v in enumerate(nums):
            if v == target:
                return i
        return -1