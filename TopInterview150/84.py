from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        monotone_stack = [-1]
        ret_val = 0

        for idx, val in enumerate(heights):
            while monotone_stack[-1] != -1 and val <= heights[monotone_stack[-1]]:
                # Current height 
                cur_height = heights[monotone_stack.pop()]
                # Current width -> last index in stack
                cur_width = idx - monotone_stack[-1] - 1
                ret_val = max(ret_val, cur_height * cur_width)

            monotone_stack.append(idx)

        return ret_val


if __name__ == "__main__":
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    # heights = [1]
    # heights = [2, 2]
    print(sol.largestRectangleArea(heights=heights))    
