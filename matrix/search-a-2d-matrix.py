class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        low, high = 0, R - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][C - 1]:
                l, r = 0, C - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    if matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            elif target < matrix[mid][0]:
                high = mid - 1
            else:  # target > matrix[mid][-1]
                low = mid + 1
        return False
