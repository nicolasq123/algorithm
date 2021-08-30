class Solution:
    def canCompleteCircuit(self, gas, cost):
        diff = [gas[i]-cost[i] for i in range(len(gas))] # 多出来多少汽油
        if sum(diff) < 0:
            return -1

        runs = [0 for _ in range(len(gas))] # 累加和
        minsum = diff[0]
        idx = 0
        for i in range(len(diff)):
            if i == 0:
                runs[i] = diff[i]
            else:
                runs[i] = runs[i-1] + diff[i]
            if runs[i] <= minsum:
                minsum = runs[i]
                idx = i
        return (idx+1) % (len(gas))