from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list and in-degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # Push all courses with 0 in-degrees into the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_count = 0
        
        while queue:
            course = queue.popleft()
            completed_count += 1
            
            # Reduce in-degree for neighboring courses
            for next_course in adj[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
        # If we can finish all courses, return True
        return completed_count == numCourses