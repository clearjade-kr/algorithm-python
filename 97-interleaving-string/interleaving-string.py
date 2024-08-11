class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if len(s3) != n1 + n2:
            return False

        # dp[i][j] : whether s1[:i] and s2[:j] can interleave to s3[:i+j]
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True

        for i in range(1, n1 + 1):
            dp[i][0] = (s1[i - 1] == s3[i - 1]) and dp[i - 1][0]

        for i in range(1, n2+1):
            dp[0][i] = (s2[i - 1] == s3[i - 1]) and dp[0][i - 1]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                t1 = (s1[i - 1] == s3[i + j - 1]) and dp[i - 1][j]
                t2 = (s2[j - 1] == s3[i + j - 1]) and dp[i][j - 1]
                dp[i][j] = t1 or t2

        return dp[n1][n2]
