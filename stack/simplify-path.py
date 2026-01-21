class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        for _ in paths:
            if not _:
                continue
            if _ == ".":
                continue
            if _ == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(_)
        return '/' + '/'.join(stack)