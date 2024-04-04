class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_point = 0
        cur_count = 1
        total_count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[cur_point]:
                nums[cur_point + 1] = nums[i]
                cur_point += 1
                cur_count = 1
                total_count -= 1
            elif cur_count == 1:
                nums[cur_point + 1] = nums[i]
                cur_point += 1
                cur_count += 1
                total_count -= 1

            else:
                cur_count += 1
                total_count += 1

        last_val = nums[cur_point - 1]
        while total_count >= 2 and cur_point < len(nums) - 1:
            nums[cur_point] = last_val
            cur_count -= 1
            cur_point += 1

        # print(nums)
        if total_count > 1:
            cur_point -= total_count
        return cur_point + 1