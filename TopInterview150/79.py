from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        n = len(board)
        m = len(board[0])

        def dfs(x, y, cur_idx):
            if cur_idx == len(word) - 1:
                return True

            cur_char = board[x][y]
            board[x][y] = '#'

            for cur_dx, cur_dy in zip(dx, dy):
                next_x = x + cur_dx
                next_y = y + cur_dy

                if 0 <= next_x < n and 0 <= next_y < m and board[next_x][next_y] == word[cur_idx + 1]:
                    if dfs(next_x, next_y, cur_idx + 1):
                        return True

            board[x][y] = cur_char
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    print(sol.exist(board, word))
