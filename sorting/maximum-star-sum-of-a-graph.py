class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = max(vals)
        for node in graph:
            contributes = [vals[k] for k in graph[node]]
            contributes.sort(reverse=True)
            temp = vals[node]
            for i in range(min(k, len(contributes))):
                if contributes[i] < 0:
                    break
                temp += contributes[i]
            res = max(res, temp)
        return res