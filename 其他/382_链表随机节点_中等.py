import random
class Solution:
    """
    水塘抽样算法： 第i个元素以1/i的概率选择该元素
    k/i * (1-k/i+1 *k) ..... = k/n
    """

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        this.head = head
        return self.getRandom()

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randint(1,10)
        i = 0
        res = -1
        p = this.head
        while p:
            i += 1
            if random.randint(1,i) == 1:
                res = p.val
            p = p.next
        return res