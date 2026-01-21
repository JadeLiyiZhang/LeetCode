class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for after, pre in prerequisites:
            graph[pre].append(after)
        
        state = [0] * numCourses
        order = []
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for nxt in graph[course]:
                if not dfs(nxt):
                    return False
            state[course] = 2
            order.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        order.reverse()
        return order
