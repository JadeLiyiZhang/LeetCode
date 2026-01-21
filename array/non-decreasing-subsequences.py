class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:
            result.append(path[:])

        used = [0] * 201
        for i in range(startIndex, len(nums)):
            if (path and nums[i] < path[-1]) or used[nums[i] + 100] == 1:
                continue

            used[nums[i] + 100] = 1
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
