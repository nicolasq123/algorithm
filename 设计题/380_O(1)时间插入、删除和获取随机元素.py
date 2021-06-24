import random

class RandomizedSet:
    """
    显然， hash + 数组
    1. insert时候数组直接append
    2. remove的时候把要remove的元素和最后的替换，然后pop
    3. random的时候直接在数组里随机取
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {} # k: val值， v: 在l中的位置
        self.l = [] # 存的val值
        self.cnt = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.data.get(val) is not None:
            return False

        self.cnt += 1
        self.l.append(val)
        self.data[val] = self.cnt -1

        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.data.get(val) is None:
            return False
        
        idx = self.data[val]
        del self.data[val]
        
        if idx == self.cnt-1:
            # 最后一个元素
            self.l.pop()
            self.cnt -=1
            return True
        
        # 被替换元素的值
        tmp = self.l[self.cnt-1]

        self.l[idx], self.l[self.cnt-1] = self.l[self.cnt-1], self.l[idx]
        self.data[tmp] = idx # 被替换到了idx位置
        self.l.pop()
        self.cnt -=1
        return True



    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = random.random()
        return self.l[int(r * self.cnt)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()