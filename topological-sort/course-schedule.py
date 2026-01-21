from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for after, pre in prerequisites:
            graph[pre].append(after)

        # 0 = unvisited, 1 = visiting (in current path), 2 = visited (done)
        state = [0] * numCourses

        def dfs(u: int) -> bool:
            if state[u] == 1:   # back edge -> cycle
                return False
            if state[u] == 2:   # already checked, no cycle from here
                return True

            state[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
