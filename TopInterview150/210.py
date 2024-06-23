from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # from collections import defaultdict, deque
        #
        # list_indegree = [0] * numCourses
        #
        # graph = defaultdict(list)
        #
        # for a, b in prerequisites:
        #     graph[b].append(a)
        #     list_indegree[a] += 1
        #
        # q = deque([i for i in range(numCourses) if list_indegree[i] == 0])
        #
        # list_explored = []
        # while q:
        #     cur_course = q.popleft()
        #     list_explored.append(cur_course)
        #
        #     for next_course in graph[cur_course]:
        #         list_indegree[next_course] -= 1
        #         if list_indegree[next_course] == 0:
        #             q.append(next_course)
        #
        # if len(list_explored) == numCourses:
        #     return list_explored
        # return []
        from collections import  defaultdict
        dic = defaultdict(list)
        for course, prereq in prerequisites:
            dic[course].append(prereq)

        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)
            for i in dic[course]:
                if not dfs(i):
                    return False
            cycle.remove(course)

            visited.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output


if __name__ == "__main__":
    sol = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(sol.findOrder(numCourses, prerequisites))




