class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for j in range(len(gas)):
            total = total + gas[j] - cost[j]
            if total < 0:
                start = j + 1
                total = 0
        return start
