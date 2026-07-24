class MinStack:

    def __init__(self):
        self.stack = [float("inf")]
        self.min_stack = [] 
        self.minimum_val = float("inf")

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if val < self.stack[-1]:
            self.stack.append(val)
        else:
            self.stack.append(self.stack[-1])
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.stack[-1]
