class Solution:

    def __init__(self, w: List[int]):
        num_sum = 0
        self.sum_flows = []
        for weight in w:
            num_sum += weight
            self.sum_flows.append(num_sum)
        self.total = num_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        left, right = 0, len(self.sum_flows)
        while left < right:
            mid = left + (right - left) // 2
            if self.sum_flows[mid] >= target:
                right = mid
            elif self.sum_flows[mid] < target:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()