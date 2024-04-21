from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail = 0, len(numbers) - 1
        while head < tail:
            cur_sum = numbers[head] + numbers[tail]
            if cur_sum < target:
                head += 1
            elif cur_sum > target:
                tail -= 1
            else:
                return [head + 1, tail + 1]


if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    target = 9
    print(sol.twoSum(numbers, target))
