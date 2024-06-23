from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_end = 0
        right_end = len(height) - 1
        max_height = max(height)
        cur_height = 1
        ret = 0
        while left_end <= right_end and cur_height <= max_height:
            while height[left_end] < cur_height:
                left_end += 1
            while height[right_end] < cur_height:
                right_end -= 1
            if left_end > right_end:
                break
            ret += right_end - left_end + 1
            cur_height += 1
        return ret - sum(height)


if __name__ == "__main__":
    sol = Solution()
    # height = [2,0,2]
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [4,2,0,3,2,5]
    height = [0,2,0]
    print(sol.trap(height))

