class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0

        while t_idx < len(t) and s_idx < len(s):
            if t[t_idx] == s[s_idx]:
                s_idx += 1
            t_idx += 1

        if s_idx == len(s):
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    s = "axc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
