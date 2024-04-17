class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # First rep : 2(n-1) + 0 + 2(n-1) + 0
        # Second rep : 2(n-2) + 2(2-1)
        # Ktb rep : 2(n-k) + 2(k-1)

        if numRows == 1 or len(s) <= numRows:
            return s

        ans = ''
        for i in range(numRows):
            
            
            first_jump = 2 * i
            second_jump = 2 * (numRows - i - 1)

            cur_idx = i
            ans = ans + s[i]
            while cur_idx < len(s):
                if second_jump != 0:
                    cur_idx += second_jump
                    if cur_idx >= len(s):
                        break
                    ans = ans + s[cur_idx]
                if first_jump != 0:
                    cur_idx += first_jump
                    if cur_idx >= len(s):
                        break
                    ans = ans + s[cur_idx]

        return ans
