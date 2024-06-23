from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        # Make board into list vs calculate position of board
        n = len(board)
        target_pos = n ** 2 - 1
        visited = [[False] * n for _ in range(n)]

        def calculate_position(pos):
            x, y = pos // n, pos % n
            if x % 2 != 0:
                y = n - 1 - y
            x = n - 1 - x
            return x, y

        queue = deque([0])
        cnt_dice = 0
        while queue:
            cur_len = len(queue)
            for _ in range(cur_len):
                cur_pos = queue.popleft()
                for i in range(1, 7):
                    next_pos = cur_pos + i
                    if cur_pos + i == target_pos:
                        return cnt_dice + 1
                    elif cur_pos + i > target_pos:
                        break
                    x, y = calculate_position(next_pos)
                    if board[x][y] != -1:
                        next_pos = board[x][y] - 1
                        if next_pos == target_pos:
                            return cnt_dice + 1
                        x, y = calculate_position(next_pos)

                    if not visited[x][y]:
                        visited[x][y] = True
                        queue.append(next_pos)
            cnt_dice += 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    # board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    # board = [[1,1,-1],[1,1,1],[-1,1,1]]
    board = [[-1,10,-1,15,-1],[-1,-1,18,2,20],[-1,-1,12,-1,-1],[2,4,11,18,8],[-1,-1,-1,-1,-1]]
    print(sol.snakesAndLadders(board))


