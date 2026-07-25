class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        key = []

        for c in path + "/":
            if c == "/":
                key = ''.join(key)
                if key == "..":
                    if stack: stack.pop()
                elif key != "" and key != ".":
                    stack.append(key)
                key = []
            else:
                key.append(c)

        return "/" + "/".join(stack)