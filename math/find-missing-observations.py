class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        _sum = mean * (m + n)
        gap = _sum - sum(rolls)

        if gap > 6 * n or gap < n:
            return []
        
        res = [1] * n
        temp_sum = n
        while temp_sum < gap:
            for i in range(n):
                if temp_sum < gap:
                    res[i] += 1
                    temp_sum += 1
        return res