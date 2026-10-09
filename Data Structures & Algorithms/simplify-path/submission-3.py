class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []

        for dir1 in dirs:
            if dir1 == "..":
                if stack:
                    stack.pop()
            elif dir1 != "" and dir1 != ".":
                stack.append(dir1)

        return "/" + "/".join(stack)