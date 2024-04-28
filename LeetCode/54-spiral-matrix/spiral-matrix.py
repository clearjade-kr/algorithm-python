class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        cur_dir = 0
        cur_rep = 0

        width = len(matrix[0])
        height = len(matrix)

        cur_width = width - cur_rep
        cur_height = height - cur_rep

        while cur_width > 1 and cur_height > 1:
            cur_x, cur_y = cur_rep, cur_rep
            for i in range(4):
                cur_len = cur_width - 1 if i % 2 == 0 else cur_height - 1
                for _ in range(cur_len):
                    ret.append(matrix[cur_y][cur_x])
                    cur_x += direction[cur_dir][0]
                    cur_y += direction[cur_dir][1]
                cur_dir = (i + 1) % 4
            cur_rep += 1
            cur_width -= 2
            cur_height -= 2

        if cur_width == 1 or cur_height == 1:
            cur_x, cur_y = cur_rep, cur_rep
            cur_len = cur_height if cur_width == 1 else cur_width
            cur_dir = 1 if cur_width == 1 else 0
            for _ in range(cur_len):
                ret.append(matrix[cur_y][cur_x])
                cur_x += direction[cur_dir][0]
                cur_y += direction[cur_dir][1]

        return ret
