class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_row = [set() for _ in range(9)]
        set_col = [set() for _ in range(9)]
        set_box = [set() for _ in range(9)]

        for i in range(9): # col
            for j in range(9): # row
                if board[i][j] != ".":
                    if board[i][j] not in set_row[j]:
                        set_row[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in set_col[i]:
                        set_col[i].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in set_box[(i // 3) * 3 + (j // 3)]:
                        set_box[(i // 3) * 3 + (j // 3)].add(board[i][j])
                    else:
                        return False
        return True