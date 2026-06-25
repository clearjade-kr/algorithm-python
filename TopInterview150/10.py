
"""
Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Dynamic programming approach
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        dp[0][1] = False
        dp[1][0] = False
        dp[1][1] = s[0] == p[0] or p[0] == '.'

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # p[j - 1] == '*' : 0 or more of the preceding element
                # We can either ignore '*' (0 element) and write with preceding element (dp[i][j - 2]) 
                # or we can use '*' to match the current character in s with (dp[i - 1][j])
                # s[i - 1] == p[j - 2] means exact match 
                # p[j - 2] == '.' means any character can match
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

                # Else we check if the characters match exactly or pattern has '.' (any character)
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

        return dp[m][n]

        # if not p:
        #     return not s

        # first_match = bool(s) and p[0] in {s[0], '.'}

        # if len(p) >= 2 and p[1] == '*':
        #     return (self.isMatch(s, p[2:]) or
        #             first_match and self.isMatch(s[1:], p))
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])



if __name__ == "__main__":
    sol = Solution()
    # test_s = 'aa'
    # test_p = 'a*'

    # test_s = 'aa'
    # test_p = '.aa'

    # test_s = 'ab'
    # test_p = '.*'

    test_s = 'aaa'
    test_p = 'a*a'

    print(sol.isMatch(test_s, test_p))
