class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rep = n // 2
        cur_len = n - 1
        for i in range(rep):
            # y, x
            left_up = [i, i]
            right_up = [i, cur_len - i]
            left_down = [cur_len - i, i]
            right_down = [cur_len - i, cur_len - i]

            for j in range(cur_len - 2 * i):
                matrix[left_up[0]][left_up[1]], matrix[right_up[0]][right_up[1]], matrix[right_down[0]][right_down[1]], matrix[left_down[0]][left_down[1]] =\
                    matrix[left_down[0]][left_down[1]], matrix[left_up[0]][left_up[1]], matrix[right_up[0]][right_up[1]], matrix[right_down[0]][right_down[1]]

                left_up[1] += 1
                right_up[0] += 1
                right_down[1] -= 1
                left_down[0] -= 1
