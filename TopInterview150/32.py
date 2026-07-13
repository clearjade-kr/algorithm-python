class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Since we cannot define from beginning, planning to use 2 dimension DP
        # dp[i][j] = s[i:j] counting '(' as stack
        # if dp[i][j-1] < 0 -> Not valid starting from i
        
        # cur_max = 0
        # cnt_close = s.count(')')
        # for i in range(len(s)):
        #     cur_stack = 0
        #     for j in range(i, len(s)):
        #         if s[j] == '(':
        #             if j > 0:
        #                 cur_stack = cur_stack + 1 if cur_stack >= 0 else -1
        #             else:
        #                 cur_stack = 1
        #         else: # if s[j] == ')'
        #             if j > 0:
        #                 cur_stack = cur_stack - 1 if cur_stack > 0 else -1
        #             else:
        #                 cur_stack = -1

        #         if cur_stack < 0:
        #             break
        #         elif cur_stack > cnt_close:
        #             break
        #         elif cur_stack == 0:
        #             cur_max = max(cur_max, j - i + 1)

        # return cur_max

        cur_max = 0
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1

            if left == right:
                cur_max = max(cur_max, left + right)
            elif right > left:
                left = right = 0
            
        left, right = 0, 0
        for i in reversed(s):
            if i == ')':
                right += 1
            else:
                left += 1
            
            if right == left:
                cur_max = max(cur_max, left + right)
            elif left > right:
                left = right = 0
            
        return cur_max


if __name__ == "__main__":
    sol = Solution()
    s = ")()())"
    print(sol.longestValidParentheses(s=s))
