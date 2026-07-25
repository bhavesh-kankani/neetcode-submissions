class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        key = []
        num = []
        for c in s:
            if c == ']':
                while stack[-1] != '[':
                    key.append(stack.pop())
                stack.pop()
                while stack and stack[-1] in "0123456789":
                    num.append(stack.pop())
                k = int(''.join(num[::-1]))
                stack.append(k*(''.join(key[::-1])))
                key = []
                num = []
            else:
                stack.append(c)
        return ''.join(stack)