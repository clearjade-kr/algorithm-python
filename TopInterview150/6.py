class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # First rep : 2(n-1) + 0 + 2(n-1) + 0
        # Second rep : 2(n-2) + 2(2-1)
        # Ktb rep : 2(n-k) + 2(k-1)

        # if numRows == 1 or len(s) <= numRows:
        #     return s
        #
        # ans = ''
        # for i in range(numRows):
        #     first_jump = 2 * i
        #     second_jump = 2 * (numRows - i - 1)
        #
        #     cur_idx = i
        #     ans = ans + s[i]
        #     while cur_idx < len(s):
        #         if second_jump != 0:
        #             cur_idx += second_jump
        #             if cur_idx >= len(s):
        #                 break
        #             ans = ans + s[cur_idx]
        #         if first_jump != 0:
        #             cur_idx += first_jump
        #             if cur_idx >= len(s):
        #                 break
        #             ans = ans + s[cur_idx]
        #
        # return ans

        if numRows == 1: return s
        out = ["" for _ in range(numRows)]
        p = 0
        dir = 0
        for c in s:
            out[p]+=c
            if p == numRows-1:
                p -= 1
                dir = -1
            elif p == 0:
                p +=1
                dir = 1
            else:
                p +=dir
        print(out)
        return "".join(out)


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3

    # s = "A"
    # numRows = 1
    print(sol.convert(s, numRows))
