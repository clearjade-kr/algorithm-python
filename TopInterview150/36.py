from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set_row = [set() for _ in range(9)]
        # set_col = [set() for _ in range(9)]
        # set_box = [set() for _ in range(9)]
        #
        # for i in range(9): # col
        #     for j in range(9): # row
        #         if board[i][j] != ".":
        #             if board[i][j] not in set_row[j]:
        #                 set_row[j].add(board[i][j])
        #             else:
        #                 return False
        #             if board[i][j] not in set_col[i]:
        #                 set_col[i].add(board[i][j])
        #             else:
        #                 return False
        #
        #             if board[i][j] not in set_box[(i // 3) * 3 + (j // 3)]:
        #                 set_box[(i // 3) * 3 + (j // 3)].add(board[i][j])
        #             else:
        #                 return False
        # return True




            # add identifying information into set in order to check for duplicates
            # within row
            # within column
            # within 3x3 block
            # use some sort of string identifier to do identify row, column, block
        seenSet = set()
        # iterate through
        for rowNum, row in enumerate(board):
            for colNum, val in enumerate(row):
                # store in seenSet
                if (val != '.'):
                    rowStr = f"{val} in row {rowNum}"
                    colStr = f"{val} in column {colNum}"
                    blockStr = f"{val} in block {rowNum//3}-{colNum//3}"
                    if (rowStr in seenSet or colStr in seenSet or blockStr in seenSet):
                        return False
                    seenSet.add(rowStr)
                    seenSet.add(colStr)
                    seenSet.add(blockStr)
        return True


if __name__ == "__main__":
    sol = Solution()
    # board = [["5","3",".",".","7",".",".",".","."]
    # ,["6",".",".","1","9","5",".",".","."]
    # ,[".","9","8",".",".",".",".","6","."]
    # ,["8",".",".",".","6",".",".",".","3"]
    # ,["4",".",".","8",".","3",".",".","1"]
    # ,["7",".",".",".","2",".",".",".","6"]
    # ,[".","6",".",".",".",".","2","8","."]
    # ,[".",".",".","4","1","9",".",".","5"]
    # ,[".",".",".",".","8",".",".","7","9"]]

    board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board))
