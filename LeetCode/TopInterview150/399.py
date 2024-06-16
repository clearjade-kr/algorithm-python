
from typing import List


# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         from collections import defaultdict
#
#         graph = defaultdict(dict)
#         for (a, b), val in zip(equations, values):
#             graph[a][b] = val
#             graph[b][a] = 1 / val
#
#         def dfs(start, end, visited):
#             if start not in graph or end not in graph:
#                 return -1.0
#
#             if start == end:
#                 return 1.0
#
#             visited.add(start)
#             for node in graph[start]:
#                 if node in visited:
#                     continue
#                 visited.add(node)
#                 val = dfs(node, end, visited)
#                 if val != -1.0:
#                     return val * graph[start][node]
#                 visited.remove(node)
#             return -1.0
#
#         res = []
#         for a, b in queries:
#             res.append(dfs(a, b, set()))
#
#         return res


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import deque

        qd = {}
        q = deque([(a,b,v) for (a,b),v in zip(equations,values)])
        while q:
            a, b, val = q.popleft()
            if (a,b) in qd: continue
            qd[(a,b)] = val

            q.append((b, a, 1 / val))
            for (c,d),nv in zip(equations, values):
                if c == b: q.append((a, d, val * nv))
                if a == d: q.append((c, b, val * nv))

        return [qd.get((a,b), -1) for a,b in queries]
