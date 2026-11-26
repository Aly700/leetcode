from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        following = [[] for _ in range(numCourses)]
        needed = [0] * numCourses
        for course, before in prerequisites:
            following[before].append(course)
            needed[course] += 1

        ready = deque(course for course in range(numCourses) if needed[course] == 0)
        finished = 0
        while ready:
            course = ready.popleft()
            finished += 1
            for next_course in following[course]:
                needed[next_course] -= 1
                if needed[next_course] == 0:
                    ready.append(next_course)

        return finished == numCourses
