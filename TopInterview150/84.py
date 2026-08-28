from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Save index closest to current and lower than current
        N = len(heights)
        left_lower = [-1] * N
        right_lower = [N] * N

        stack_left = []
        stack_right = []
        for i in range(N):
            while stack_left and heights[stack_left[-1]] > heights[i]:
                target_idx = stack_left.pop()
                right_lower[target_idx] = i

            while stack_right and heights[stack_right[-1]] > heights[N - 1 - i]:
                target_idx = stack_right.pop()
                left_lower[target_idx] = N - 1 - i

            stack_left.append(i)
            stack_right.append(N - 1 - i)

        ret_val = 0
        for idx, val in enumerate(heights):
            cur_val = val * (right_lower[idx] - left_lower[idx] - 1)
            ret_val = max(ret_val, cur_val)

        return ret_val


if __name__ == "__main__":
    sol = Solution()
    # heights = [2, 1, 5, 6, 2, 3]
    heights = [1]
    # heights = [2, 2]
    print(sol.largestRectangleArea(heights=heights))    
