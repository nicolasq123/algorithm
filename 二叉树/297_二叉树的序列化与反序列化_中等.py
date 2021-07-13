"""
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:

    def serialize(self, root):
        """
        1. 前序遍历，用'#'标记None， ’，‘标记分割
        2. 反序列化即可
        """
        if root is None:
            return '#'
        
        return str(root.val) + ',' + self.serialize(root.left)+ ',' + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        return self.help()

    def help(self):
        if len(self.data) == 0:
            return None
        
        if self.data[0] == '#':
            self.data = self.data[2:]
            return None
        c = self.getData(self.data)
        n = TreeNode(int(c))
        self.data = self.data[len(c)+1:]
        n.left = self.deserialize(self.data)
        n.right = self.deserialize(self.data)
        return n

    def getData(self, data):
        c = data.split(',')
        return c[0]