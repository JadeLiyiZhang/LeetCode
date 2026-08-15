class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid
        l, r = 0, col - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[left][mid] == target:
                return True
            elif matrix[left][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
