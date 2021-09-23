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


class Solution2:
    """
    双向BFS处理加速
    """
    def openLock(self, deadends, target):
        start = "0000"
        if target in deadends:
            return -1
        if start in deadends:
            return -1
        if start == target:
            return 0
        return self.bbfs(deadends, start, target)

        
    def bbfs(self, deadends, start, target):
        dead_dict = {}
        for d in deadends:
            dead_dict[d] = True
        
        visited = {}
        q1 = set([start])
        q2 = set([target])

        depth = 0
        while q1 and q2:
            if len(q2) <= len(q1):
                q1, q2 = q2, q1 

            new_q = []
            for s in q1:
                visited[s] = s # 拿出来的时候才visited,避免一边add，另一边add不进去
                if s in dead_dict:
                    continue
                if s in q2:
                    return depth

                for n in self.next_str(s):
                    if n not in visited:
                        new_q.append(n)

            q1 = set(new_q)
            depth += 1
        return -1

    def next_str(self, s):
        res = []
        for i in range(len(s)):
            a, b = self.next_char(s[i])
            res.append(s[:i] + a + s[i+1:])
            res.append(s[:i] + b + s[i+1:])
        return res
    
    def next_char(self, c):
        """
        邻居字符
        """
        if c == '0':
            return ['1', '9']
        if c == '9':
            return ['0', '8']
        return [str(int(c)+1), str(int(c)-1)]



if __name__ == '__main__':
    #print(Solution2().next_str("1234"))
    print(Solution2().openLock(["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"], "5555"))
    #print(Solution2().openLock(["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"], "5555"))