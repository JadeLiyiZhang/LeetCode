class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backtracking(k, n, 1, 0, res, [])
        return res
    
    def backtracking(self, k, n, startIndex, sum, res, path):
        if sum > n:
            return
        
        if sum == n and len(path) == k:
            res.append(path[:])
            return

        for i in range(startIndex, 10):
            sum += i
            path.append(i)
            self.backtracking(k, n, i + 1, sum, res, path)
            temp = path.pop()
            sum -= temp