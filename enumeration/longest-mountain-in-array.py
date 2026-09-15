class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        right_lower = [0] * len(arr)
        left_lower = [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                right_lower[i] = right_lower[i - 1] + 1
            else:
                right_lower[i] = 0
        
        for j in range(len(arr) - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                left_lower[j] = left_lower[j + 1] + 1
            else:
                left_lower[j] = 0
        res = 0
        for k in range(0, len(arr)):
            if right_lower[k] == 0 or left_lower[k] == 0:
                continue
            res = max(res, left_lower[k] + right_lower[k] + 1)
        return res if res >= 3 else 0
