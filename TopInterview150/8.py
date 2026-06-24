class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        sign = 1
        if s and s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        str_val = ''
        for c in s:
            if c.isdigit():
                str_val += c
            else:
                break

        if not str_val:
            return 0
        ret_val = int(str_val) * sign
        if ret_val < -2**31:
            return -2**31
        elif ret_val > 2**31 - 1:
            return 2**31 - 1
        else:
            return ret_val


if __name__ == "__main__":
    sol = Solution()
    testval = "   -42"
    print(sol.myAtoi(testval))
