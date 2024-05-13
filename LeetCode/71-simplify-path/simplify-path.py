class Solution:
    def simplifyPath(self, path: str) -> str:
        list_dirs = path.split("/")
        stack_path = []
        for d in list_dirs:
            if not d or d == '.':
                continue
            if d == "..":
                if stack_path:                
                    stack_path = stack_path[:len(stack_path) - 1]
            else:
                stack_path.append(d)

        return "/%s" % "/".join(stack_path)