class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start, end = 0, 0

        cur_set = set()
        while end < len(s):
            if s[end] not in cur_set:
                cur_set.add(s[end])
                ans = max(ans, end - start + 1)
                end += 1
            else:
                cur_set.remove(s[start])
                start += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "abcbcdef"
    print(sol.lengthOfLongestSubstring(s))