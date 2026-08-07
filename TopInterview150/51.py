from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking with having board as parameter
        ret_queens = []

        def check_idx(list_queens, i, j):
            for s in range(n):
                if (i, s) in list_queens or (s, j) in list_queens:
                    return False
                target_diagonals = [(i + s, j + s), (i - s, j + s), (i - s, j - s), (i + s, j - s)]
                for target in target_diagonals:
                    if 0 <= target[0] < n and 0 <= target[1] < n and target in list_queens:
                        return False
            return True

        def backtrack(list_queens):
            if len(list_queens) == n:
                ret_queens.append(list_queens.copy())
                return

            i = len(list_queens)
            for j in range(n):
                if not check_idx(list_queens=list_queens, i=i, j=j):
                    continue

                list_queens.append((i, j))
                backtrack(list_queens=list_queens)
                list_queens.pop()

        backtrack([])

        list_boards = []
        for queens in ret_queens:
            board = ['.' * n for _ in range(n)]
            for queen in queens:
                board[queen[0]] = board[queen[0]][:queen[1]] + 'Q' + board[queen[0]][queen[1] + 1:]

            list_boards.append(board)

        return list_boards


if __name__ == "__main__":
    sol = Solution()
    n = 4
    boards = sol.solveNQueens(n)
    for board in boards:
        print(board)
