from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking with having board as parameter
        ret_queens = []

        # Plan to place queens each rows
        # set_col: columns having queen
        # set_rd : right down diagonal queen - right diagonal have same row - column value
        # set_ld : left down diagonal queen - left diagonal have same row + column value

        set_col = set()
        set_rd = set()
        set_ld = set()

        def check_idx(row, col):
            if col in set_col:
                return False
            if row - col in set_rd:
                return False
            if row + col in set_ld:
                return False
            return True
            
        def backtrack(list_col):
            if len(list_col) == n:
                ret_queens.append(list_col.copy())
                return

            row = len(list_col)
            for col in range(n):
                if not check_idx(row=row, col=col):
                    continue

                list_col.append(col)
                set_col.add(col)
                set_rd.add(row - col)
                set_ld.add(row + col)

                backtrack(list_col=list_col)

                list_col.pop()
                set_col.remove(col)
                set_rd.remove(row - col)
                set_ld.remove(row + col)

        backtrack([])

        list_boards = []
        for queens in ret_queens:
            board = ['.' * n for _ in range(n)]
            for i in range(len(queens)):
                board[i] = '.' * queens[i] + 'Q' + '.' * (n - queens[i] - 1)

            list_boards.append(board)

        return list_boards


if __name__ == "__main__":
    sol = Solution()
    n = 4
    boards = sol.solveNQueens(n)
    for board in boards:
        print(board)
