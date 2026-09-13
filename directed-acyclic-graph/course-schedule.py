from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_seq = defaultdict(list)
        for after, pre in prerequisites:
            course_seq[pre].append(after)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for next_course in course_seq[course]:
                if not dfs(visited[course]):
                    return False
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True