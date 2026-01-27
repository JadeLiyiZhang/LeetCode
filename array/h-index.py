class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)

        # count frequencies
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        
        # paper: number of papers with citations >= i
        paper = 0
        for i in range(n, -1, -1):
            paper += bucket[i]
            if paper >= i:
                return i
        return 0
        
