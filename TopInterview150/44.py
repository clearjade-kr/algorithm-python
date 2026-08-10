class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ? = any single char / * = any multiple char
        # 2-dimensional DP approach
        # dp[i][j]: s[:i] matches the pattern p[:j]

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    # s = "aa"
    # p = "aa"
    # s = "adceb"
    # p = "*a*b"
    # s = "a"
    # p = "*"
    s = ""
    p = "*****"
    print(sol.isMatch(s = s, p = p))
