"""
https://leetcode-cn.com/problems/open-the-lock/
"""
import collections
class Solution:

    def openLock(self, deadends, target):
        start = "0000"
        if target in deadends:
            return -1
        if start in deadends:
            return -1
        if start == target:
            return 0
        
        visited = {}
        visited[start] = True
        dead_dict = {}
        for d in deadends:
            dead_dict[d] = True

        queue = collections.deque([])
        queue.append(start)
        depth = 0
        while len(queue) != 0:
            l = len(queue)
            for i in range(l):
                item = queue.popleft()
                if item == target:
                    return depth

                for tmp in self.next_str(item):
                    if dead_dict.get(tmp):
                        continue
                    if visited.get(tmp):
                        continue
                    visited[tmp] = True
                    queue.append(tmp)
            depth +=1
        return -1
    
    def next_char(self, c):
        """
        邻居字符
        """
        if c == '0':
            return ['1', '9']
        if c == '9':
            return ['0', '8']
        return [str(int(c)+1), str(int(c)-1)]
    
    def next_str(self, s):
        res = []
        for i in range(len(s)):
            a, b = self.next_char(s[i])
            res.append(s[:i] + a + s[i+1:])
            res.append(s[:i] + b + s[i+1:])
        return res
