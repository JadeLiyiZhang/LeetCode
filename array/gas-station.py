class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [0] * len(gas)
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        total = 0
        start = 0
        for j in range(len(gas)):
            total = total + diff[j]
            if total < 0:
                start = j + 1
                total = 0
        return start
