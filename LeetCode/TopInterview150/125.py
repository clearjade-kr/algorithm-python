class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        s = s.lower()

        while start < len(s) and not s[start].isalnum():
            start += 1

        while end >= 0 and not s[end].isalnum():
            end -= 1

        while start <= end:
            if s[start] != s[end]:
                return False

            start += 1
            while start < len(s) and not s[start].isalnum():
                start += 1

            end -= 1
            while end >= 0 and not s[end].isalnum():
                end -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    # s = " "
    print(sol.isPalindrome(s))
