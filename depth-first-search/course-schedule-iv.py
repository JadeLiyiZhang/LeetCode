class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for pre, post in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1
        
        # topo sorting
        table = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                table.append(i)
        
        topo = []
        while table:
            u = table.popleft()
            topo.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    table.append(v)

        isPre = [[False] * numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            isPre[a][b] = True
        
        for u in reversed(topo):
            for v in graph[u]:
                for k in range(numCourses):
                    if isPre[v][k]:
                        isPre[u][k] = True
        
        res = []
        for i, j in queries:
            if isPre[i][j]:
                res.append(True)
            else:
                res.append(False)
        return res
        

