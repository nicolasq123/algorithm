package main

import "fmt"

func main() {
	fmt.Println("4.5.0" >= "4.4.1")
}



class Solution:
    def isValid(self, s: str):
		n = len(s)
        if n % 2 == 1:
            return False
		
		a = 0
		b = 0
		c = 0

        import collections
        deq = collections.deque([])
        for i in range(n):
            if s[i] in ["(", "{", "["]:
                deq.append(s[i])
                continue
            
            if len(deq) == 0:
                return False
            c = deq.pop()

            if (c + s[i]) not in ["()", "{}", "[]"]:
                return False
        
        return len(deq) == 0