class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if self.check(mid, citations):
                res = mid
                left = mid + 1
            elif not self.check(mid, citations):
                right = mid - 1
        return res

    def check(self, num, citations):
        count = 0
        for citation in citations:
            if citation >= num:
                count += 1
        return count >= num