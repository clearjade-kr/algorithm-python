class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        list_visit = [False] * numCourses
        list_stack = [False] * numCourses

        def dfs(course):
            list_visit[course] = True
            list_stack[course] = True
            for v in graph[course]:
                if not list_visit[v]:
                    if not dfs(v):
                        return False
                elif list_stack[v]:
                    return False
            list_stack[course] = False
            return True

        for i in range(numCourses):
            if not graph[i]:
                continue
            if not list_visit[i] and not dfs(i):
                return False

        return True
