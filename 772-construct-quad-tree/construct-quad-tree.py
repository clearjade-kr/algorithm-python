class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(cur_x, cur_y, cur_size):
            flag_val = grid[cur_x][cur_y]
            flag_check = True

            for i in range(cur_x, cur_x + cur_size):
                if not flag_check:
                    break
                for j in range(cur_y, cur_y + cur_size):
                    if not flag_check:
                        break
                    if grid[i][j] != flag_val:
                        flag_check = False
                        break

            cur_node = Node(val=flag_val, isLeaf=flag_check,
                            topLeft=None, topRight=None,
                            bottomLeft=None, bottomRight=None)
            if not flag_check:
                next_size = cur_size // 2
                bottom_left = dfs(cur_x + next_size, cur_y, next_size)
                bottom_right = dfs(cur_x + next_size, cur_y + next_size, next_size)
                top_left = dfs(cur_x, cur_y, next_size)
                top_right = dfs(cur_x, cur_y + next_size, next_size)

                cur_node.bottomLeft = bottom_left
                cur_node.bottomRight = bottom_right
                cur_node.topLeft = top_left
                cur_node.topRight = top_right

            return cur_node

        return dfs(0, 0, len(grid))