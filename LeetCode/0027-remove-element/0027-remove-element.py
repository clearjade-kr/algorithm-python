class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                cnt += 1
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[end] == "_":
                end -= 1
                continue

            if nums[start] != "_":
                start += 1
                continue

            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

        # print(nums)
        return len(nums) - cnt