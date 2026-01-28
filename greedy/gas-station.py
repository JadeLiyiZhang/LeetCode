class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        start = 0
        oil = 0
        for i in range(n):
            if oil + gas[i] < cost[i]:
                start = i + 1
                oil = 0
            else:
                oil = oil + gas[i] - cost[i]
        return start
        
