class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        list_change = []
        list_dir = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)]

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                cnt_nbr = 0
                for cur_dir in list_dir:
                    next_i, next_j = i + cur_dir[0], j + cur_dir[1]
                    if 0 <= next_i < m and 0 <= next_j < n:
                        cnt_nbr += board[next_i][next_j]
                if board[i][j] == 0:
                    if cnt_nbr == 3:
                        list_change.append((i, j))
                else:
                    if cnt_nbr < 2 or cnt_nbr > 3:
                        list_change.append((i, j))

        for target in list_change:
            board[target[0]][target[1]] = int(board[target[0]][target[1]] == 0)