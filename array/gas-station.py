class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        n = len(gas)
        start = 0
        tank = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            if tank + diff < 0:
                start = i + 1
                tank = 0
            else:
                tank += diff
            total += diff
        return start if total >= 0 else -1