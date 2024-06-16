from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        list_col = set()
        list_row = set()
        for i in range(len(matrix)): # i : row (y)
            for j in range(len(matrix[0])): # j : col (x)
                if matrix[i][j] == 0:
                    list_row.add(i)
                    list_col.add(j)

        for i in list_row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        for j in list_col:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        # for mat in matrix:
        #     print(mat)


if __name__ == "__main__":
    sol = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(matrix)
