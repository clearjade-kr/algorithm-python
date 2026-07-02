class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        
        if divisor == -1:
            if dividend == -2 ** 31:
                return 2 ** 31 - 1
            else:
                return -1 * dividend

        quotient = 0
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend < divisor:
            return 0

        while dividend >= divisor * (quotient + 1):
            sub_quotient = 1
            while dividend >= divisor * (quotient + sub_quotient * 2):
                sub_quotient *= 2
            quotient += sub_quotient

        return quotient * sign


if __name__ == "__main__":
    sol = Solution()
    dividend = -7
    divisor = 2
    print(sol.divide(dividend=dividend, divisor=divisor))
