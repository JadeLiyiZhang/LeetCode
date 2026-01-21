class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness = sorted(happiness, reverse=True)
        for i in range(k):
            happiness[i] -= i
            if happiness[i] > 0:
                res += happiness[i]

            else:
                continue
        
        return res