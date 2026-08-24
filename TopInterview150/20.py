class Solution:
    def isValid(self, s: str) -> bool:
        # Check length of s is even
        if len(s) % 2 != 0:
            return False

        # map for matching brackets
        matching = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()  # O(1) pop
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    s = "({"
    print(sol.isValid(s))
