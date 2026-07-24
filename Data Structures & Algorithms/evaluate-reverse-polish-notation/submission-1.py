class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for x in tokens:
            if x in operators:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(eval(str(b) + x + str(a))))
            else:
                stack.append(x)
            print(stack)
        return int(stack.pop())