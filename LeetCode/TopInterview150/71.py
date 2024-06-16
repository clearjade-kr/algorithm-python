class Solution:
    def simplifyPath(self, path: str) -> str:
        list_dirs = path.split("/")
        stack_path = []
        for d in list_dirs:
            if not d or d == '.':
                continue
            if d == "..":
                if stack_path:
                    stack_path.pop()
            else:
                stack_path.append(d)

        return f"/{'/'.join(stack_path)}"


if __name__ == "__main__":
    sol = Solution()
    path = "/home/user/Documents/../Pictures"
    print(sol.simplifyPath(path))
