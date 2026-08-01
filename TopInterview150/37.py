from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # DFS style approach?

        # [0][1][2]
        # [3][4][5]
        # [6][7][8]

        # Recursion approach, start from 0, 0
        # If board[i, j] = .
        # Check row, col, box 
        # If i, j has reached end, return

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        empty_points = []

        for i in range(9):
            for j in range(9):
                box_idx = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    row_set[i].add(board[i][j])
                    col_set[j].add(board[i][j])
                    box_set[box_idx].add(board[i][j])
                else:
                    empty_points.append((i, j))
        

        def solve(index):
            for i, j in empty_points[index:]:
                box_idx = (i // 3) * 3 + j // 3
                for target in '123456789':
                    if target in row_set[i]:
                        continue
                    elif target in col_set[j]:
                        continue
                    elif target in box_set[box_idx]:
                        continue
                
                    row_set[i].add(target)
                    col_set[j].add(target)
                    box_set[box_idx].add(target)

                    board[i][j] = target
                    if solve(index + 1):
                        return True
                    board[i][j] = '.'
                    row_set[i].remove(target)
                    col_set[j].remove(target)
                    box_set[box_idx].remove(target)

                # No valid value for current point, return False
                return False

            # All points are filled, return True
            return True
                    
        solve(index=0)
        

if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board=board)
    for line in board:
        print(line)
