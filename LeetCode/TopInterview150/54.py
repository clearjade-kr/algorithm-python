from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # ret = []
        # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        #
        # cur_dir = 0
        # cur_rep = 0
        #
        # width = len(matrix[0])
        # height = len(matrix)
        #
        # cur_width = width - cur_rep
        # cur_height = height - cur_rep
        #
        # while cur_width > 1 and cur_height > 1:
        #     cur_x, cur_y = cur_rep, cur_rep
        #     for i in range(4):
        #         cur_len = cur_width - 1 if i % 2 == 0 else cur_height - 1
        #         for _ in range(cur_len):
        #             ret.append(matrix[cur_y][cur_x])
        #             cur_x += direction[cur_dir][0]
        #             cur_y += direction[cur_dir][1]
        #         cur_dir = (i + 1) % 4
        #     cur_rep += 1
        #     cur_width -= 2
        #     cur_height -= 2
        #
        # if cur_width == 1 or cur_height == 1:
        #     cur_x, cur_y = cur_rep, cur_rep
        #     cur_len = cur_height if cur_width == 1 else cur_width
        #     cur_dir = 1 if cur_width == 1 else 0
        #     for _ in range(cur_len):
        #         ret.append(matrix[cur_y][cur_x])
        #         cur_x += direction[cur_dir][0]
        #         cur_y += direction[cur_dir][1]
        #
        # return ret
        row=len(matrix)
        col=len(matrix[0])
        startrow=0
        endrow=row-1
        startcol=0
        endcol=col-1
        count=0
        total=row*col
        op=[]
        while count<total:
            for ind in range(startcol,endcol+1):
                if count<total:
                    op.append(matrix[startrow][ind])
                    count+=1
            startrow+=1
            for ind in range(startrow,endrow+1):
                if count<total:
                    op.append(matrix[ind][endcol])
                    count+=1
            endcol-=1
            for ind in range(endcol,startcol-1,-1):
                if count<total:
                    op.append(matrix[endrow][ind])
                    count+=1
            endrow-=1
            for ind in range(endrow,startrow-1,-1):
                if count<total:
                    op.append(matrix[ind][startcol])
                    count+=1
            startcol+=1
        print(op)
        return op


if __name__ == "__main__":
    sol = Solution()
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    # matrix = [[1,2,3],[4,5,6],[7,8,9]]

    # matrix = [[1]]
    matrix = [[3],[2]]
    print(sol.spiralOrder(matrix))
