import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Simple mathematics
        # Needs m - 1 down and n - 1 right
        # Hence, only need to select m - 1 in m + n - 2
        # (m + n - 2) C (m - 1)
        return math.comb(m + n - 2, m - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3,7))
