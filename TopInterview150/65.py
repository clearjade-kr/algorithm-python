class Solution:
    def isNumber(self, s: str) -> bool:

        # digit, dot, exponent flag
        check_digit, check_dot, check_exp = False, False, False
        s = s.lower()
        for i, ch in enumerate(s):
            # If number, flag digit
            if ch.isdigit():
                check_digit = True
            # If sign, check index and previous character is exponent
            elif ch in "+-":
                if i > 0 and s[i - 1] != 'e':
                    return False
            # If dot, check dot flag and exponent flag
            # dot cannot exist after another dot or exponent
            elif ch == '.':
                if check_dot or check_exp:
                    return False
                check_dot = True
            # If exponent, check exp flag and digit flag
            # exponent mark can only have one and after any digit
            elif ch == 'e':
                if check_exp or not check_digit:
                    return False
                check_exp = True
                check_digit = False
            else:
                return False

        # Return check_digit since at least one digit must exist
        return check_digit


if __name__ == "__main__":
    sol = Solution()
    s = "e3"
    print(sol.isNumber(s=s))
