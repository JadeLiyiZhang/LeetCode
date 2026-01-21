class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])

        def dfs(cur, visited):
            visited[cur] = 1
            if sum(visited) == n:
                return True
            res = False
            for child in graph[cur]:
                if visited[child] == 0:
                    res = dfs(child, visited)
            return res

        graph = defaultdict(set)
        for time, u, v in logs:
            graph[u].add(v)
            graph[v].add(u)

            if dfs(cur=0, visited=[0] * n):
                return time
        return -1