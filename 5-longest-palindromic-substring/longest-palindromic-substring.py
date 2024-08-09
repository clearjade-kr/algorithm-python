class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        elif len(s) == 2:
            return s if s[0] == s[1] else s[0]
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = 0
        start = 0
        end = 0

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j]:
                    if i - j < 3:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j + 1][i - 1]

                if dp[j][i] and i - j + 1 > max_len:
                    max_len = i - j + 1
                    start = j
                    end = i

        return s[start:end+1]
