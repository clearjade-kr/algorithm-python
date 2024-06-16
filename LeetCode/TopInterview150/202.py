class Solution:
    def isHappy(self, n: int) -> bool:
        list_squares = []
        i = 0
        while i < 10:
            list_squares.append(i ** 2)
            i += 1

        sum_val = 0
        set_sums = set()
        cur_n = n
        while True:
            while cur_n > 0:
                remainder = cur_n % 10
                sum_val += remainder ** 2
                cur_n = cur_n // 10

            if sum_val in set_sums:
                return False
            elif sum_val == 1:
                return True

            set_sums.add(sum_val)
            cur_n = sum_val
            sum_val = 0


if __name__ == "__main__":
    sol = Solution()
    n = 19
    print(sol.isHappy(n))
