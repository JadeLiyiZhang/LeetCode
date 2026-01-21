class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                div = arr[i] / arr[j]
                res.append((i, j, div))

        res = sorted(res, key=lambda x: x[2])
        return [arr[res[k-1][0]], arr[res[k-1][1]]]