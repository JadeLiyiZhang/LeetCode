from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        course_seq = defaultdict(list)
        for after, pre in prerequisites:
            course_seq[pre].append(after)
            indegree[after] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            
            for next_course in course_seq[cur]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        return count == numCourses
