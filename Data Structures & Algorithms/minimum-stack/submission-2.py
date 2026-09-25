class MinStack:

    def __init__(self):
        self.stack = [] # normal stack 
        self.min_stack = [float("inf")] # stores min of the self.stack at that point

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
