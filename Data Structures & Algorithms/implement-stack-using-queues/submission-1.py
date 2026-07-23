class MyStack:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push(self, x: int) -> None:
        while not self.empty():
            self.d2.append(self.pop())
        self.d1.append(x)
        
        while len(self.d2):
            self.d1.append(self.d2.popleft())
        print(self.d1)

    def pop(self) -> int:
        return self.d1.popleft()

    def top(self) -> int:
        return self.d1[0]

    def empty(self) -> bool:
        return len(self.d1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()