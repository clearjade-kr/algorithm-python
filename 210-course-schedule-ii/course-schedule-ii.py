class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque

        list_indegree = [0] * numCourses

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)
            list_indegree[a] += 1

        q = deque([i for i in range(numCourses) if list_indegree[i] == 0])

        list_explored = []
        while q:
            cur_course = q.popleft()
            list_explored.append(cur_course)

            for next_course in graph[cur_course]:
                list_indegree[next_course] -= 1
                if list_indegree[next_course] == 0:
                    q.append(next_course)

        if len(list_explored) == numCourses:
            return list_explored
        return []