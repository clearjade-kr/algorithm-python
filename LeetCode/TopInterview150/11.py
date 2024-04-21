from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_left, max_right = 0, len(height) - 1
        max_size = (max_right - max_left) * min(height[max_left],
                                                height[max_right])
        while start < end:
            size = (end - start) * min(height[start], height[end])
            if size > max_size:
                max_left, max_right, max_size = start, end, size
            else:
                if height[start] < height[end]:
                    start += 1
                else:
                    end -= 1
        return max_size


if __name__ == "__main__":
    sol = Solution()
    # height = [1,8,6,2,5,4,8,3,7]
    height = [1,1]
    print(sol.maxArea(height))
