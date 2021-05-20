"""
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/submissions/
"""
import collections

class Solution:
    def minDepth(self, root):
        """
        BFS
        """
        if root is None:
            return 0
        queue = collections.deque([])
        queue.append(root)
        depth = 1
        while len(queue) != 0:
            l = len(queue)
            for i in range(l):
                item = queue.popleft()

                if item.left is None and item.right is None: return depth
                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)
            depth +=1
        return depth