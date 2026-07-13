class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_num1, len_num2 = len(num1), len(num2)
        len_total = len_num1 + len_num2
        mult_arr = [0] * len_total

        for i in range(len_num1):
            i_val = int(num1[len_num1 - 1 - i])
            for j in range(len_num2):
                j_val = int(num2[len_num2 - 1 - j])
                cur_val = i_val * j_val
                mult_arr[len_total - 1 - i - j] += cur_val % 10
                if mult_arr[len_total - 1 - i - j] >= 10:
                    mult_arr[len_total - 1 - i - j - 1] += 1
                    mult_arr[len_total - 1 - i - j] -= 10
                mult_arr[len_total - 1 - i - j - 1] += cur_val // 10
                if mult_arr[len_total - 1 - i - j - 1] >= 10:
                    mult_arr[len_total - 1 - i - j - 2] += 1
                    mult_arr[len_total - 1 - i - j - 1] -= 10

        start_idx = 0
        while start_idx < len_total and mult_arr[start_idx] == 0:
            start_idx += 1
        ret_str = "".join(map(str, mult_arr[start_idx:]))
        return ret_str if ret_str else "0"
    

if __name__ == "__main__":
    sol = Solution()
    # num1 = "123"
    # num2 = "456"

    num1 = "9"
    num2 = "9"
    print(sol.multiply(num1=num1, num2=num2))

