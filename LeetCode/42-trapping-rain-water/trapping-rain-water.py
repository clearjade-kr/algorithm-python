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
