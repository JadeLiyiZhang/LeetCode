class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 0
        for i in range(len(citations)):
            h = min((len(citations) - i), citations[i])
            res = max(res, h)
        return res