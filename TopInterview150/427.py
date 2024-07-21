from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# class Solution:
#     def construct(self, grid: List[List[int]]) -> 'Node':
#
#         def dfs(cur_x, cur_y, cur_size):
#             flag_val = grid[cur_x][cur_y]
#             flag_check = True
#
#             for i in range(cur_x, cur_x + cur_size):
#                 if not flag_check:
#                     break
#                 for j in range(cur_y, cur_y + cur_size):
#                     if not flag_check:
#                         break
#                     if grid[i][j] != flag_val:
#                         flag_check = False
#                         break
#
#             cur_node = Node(val=flag_val, isLeaf=flag_check,
#                             topLeft=None, topRight=None,
#                             bottomLeft=None, bottomRight=None)
#             if not flag_check:
#                 next_size = cur_size // 2
#                 bottom_left = dfs(cur_x + next_size, cur_y, next_size)
#                 bottom_right = dfs(cur_x + next_size, cur_y + next_size, next_size)
#                 top_left = dfs(cur_x, cur_y, next_size)
#                 top_right = dfs(cur_x, cur_y + next_size, next_size)
#
#                 cur_node.bottomLeft = bottom_left
#                 cur_node.bottomRight = bottom_right
#                 cur_node.topLeft = top_left
#                 cur_node.topRight = top_right
#
#             return cur_node
#
#         return dfs(0, 0, len(grid))


class Solution:
    def isGridPure(self, grid: List[List[int]]) -> bool:
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                seen.add(grid[i][j])
                if len(seen) > 1:
                    return False
        return True

    def construct(self, grid: List[List[int]]) -> 'Node':
        m = len(grid)
        n = len(grid[0])
        if n > 0 and m > 0:
            if self.isGridPure(grid):
                return Node(val=grid[0][0], isLeaf=True)
            else:
                node = Node(val=0, isLeaf=False)
                node.topLeft = self.construct([q[:n//2] for q in grid[:m//2]])
                node.topRight = self.construct([q[n//2:] for q in grid[:m//2]])
                node.bottomLeft = self.construct([q[:n//2] for q in grid[m//2:]])
                node.bottomRight = self.construct([q[n//2:] for q in grid[m//2:]])
                return node


if __name__ == "__main__":
    sol = Solution()
    grid = [[0,1],[1,0]]
    sol_node = sol.construct(grid)
    print(sol_node)
