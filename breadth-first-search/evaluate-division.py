class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (src, dst), value in zip(equations, values):
            if src not in graph:
                graph[src] = {}
            if dst not in graph:
                graph[dst] = {}
            graph[src][dst] = value
            graph[dst][src] = 1 / value


        def dfs(src, dst, seen):
            if src not in graph or dst not in graph:
                return -1
            if src == dst:
                return 1
            
            for nxt in graph[src]:
                if nxt in seen:
                    continue
                seen.add(nxt)
                res = dfs(nxt, dst, seen)
                if res != -1:
                    res = res * graph[src][nxt]
                    return res
            return -1

        ans = []
        for i, j in queries:
            num = dfs(i, j, set())
            ans.append(num)
        return ans