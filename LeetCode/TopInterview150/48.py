from typing import List


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


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1]]

    # matrix = [[1,2,3],[4,5,6],[7,8,9]]

    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(matrix)
    for mat in matrix:
        print(mat)
