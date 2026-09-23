class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for x in s:
            if x == ']':
                res = []
                while stack and stack[-1] != '[':
                    res.append(stack.pop())
                stack.pop()
                integer = []
                while stack and stack[-1] in "0123456789":
                    integer.append(stack.pop())
                integer = int("".join(integer[::-1]))
                res *= integer
                stack.append("".join(res[::-1]))
            else:
                stack.append(x)
        return "".join(stack)