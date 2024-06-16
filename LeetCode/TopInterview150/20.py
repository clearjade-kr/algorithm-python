class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        while s:
            while s and s[0] not in ")}]":
                stack.append(s[0])
                s = s[1:]

            if not stack:
                return False
            elif not s:
                break

            if s[0] == '}' and stack[-1] != '{':
                return False
            elif s[0] == ')' and stack[-1] != '(':
                return False
            elif s[0] == ']' and stack[-1] != '[':
                return False

            s = s[1:]
            stack = stack[:len(stack) - 1]

        return not stack


if __name__ == "__main__":
    sol = Solution()
    s = "({"
    print(sol.isValid(s))
