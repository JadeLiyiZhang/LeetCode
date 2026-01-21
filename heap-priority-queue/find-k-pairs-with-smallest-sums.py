import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        m, n = len(nums1), len(nums2)
        k = min(k, m * n)

        # 堆元素: (sum, i, j)，只种子化每行的第一对 (i, 0)
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(m, k))]
        heapq.heapify(heap)

        res = []
        while len(res) < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:  # 同一行推进到下一个 j
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return res
