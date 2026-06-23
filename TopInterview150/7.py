class Solution:
    def reverse(self, x: int) -> int:
        '''
        Example 1:

        Input: x = 123
        Output: 321
        Example 2:

        Input: x = -123
        Output: -321
        Example 3:

        Input: x = 120
        Output: 21
        '''

        return_val = -1 * int(str(x)[:0:-1]) if str(x)[0] == '-' else int(str(x)[::-1])

        def check_range(x):
            if x < 2:
                return x
            x //= 2
            return check_range(x) + 1

        if return_val < 0:
            if check_range(return_val * -1) >= 32:
                return 0
            else: return return_val
        elif check_range(return_val) >= 32:
                return 0
        else:
            return return_val
    

if __name__ == "__main__":
    sol = Solution()
    testval=1563847412
    print(sol.reverse(testval))