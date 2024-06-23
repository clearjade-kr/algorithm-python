from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # from collections import defaultdict
        #
        # graph = defaultdict(list)
        #
        # for a, b in prerequisites:
        #     graph[a].append(b)
        #
        # list_visit = [False] * numCourses
        # list_stack = [False] * numCourses
        #
        # def dfs(course):
        #     list_visit[course] = True
        #     list_stack[course] = True
        #     for v in graph[course]:
        #         if not list_visit[v]:
        #             if not dfs(v):
        #                 return False
        #         elif list_stack[v]:
        #             return False
        #     list_stack[course] = False
        #     return True
        #
        # for i in range(numCourses):
        #     if not graph[i]:
        #         continue
        #     if not list_visit[i] and not dfs(i):
        #         return False
        #
        # return True
        from collections import defaultdict, deque
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        courses_explored = 0

        while q:
            course = q.popleft()
            courses_explored += 1

            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        return courses_explored == numCourses
