class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        remain = 0
        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
            else:
                remain = gas[i] + remain - cost[i]
        return start if start < len(gas) else -1
