class FreqStack:
    def __init__(self):
        self.hash = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.hash[val] += 1
        self.max_freq = max(self.max_freq, self.hash[val])
        self.stacks[self.hash[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.hash[val] -= 1
        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()