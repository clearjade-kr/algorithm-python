class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_digit = len(digits) - 1
        while cur_digit >= 0:
            if digits[cur_digit] == 9:
                digits[cur_digit] = 0
                if cur_digit == 0:
                    digits = [1] + digits
                    return digits
                cur_digit -= 1
            else:
                digits[cur_digit] += 1
                return digits
