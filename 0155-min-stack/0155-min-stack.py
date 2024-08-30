class MinStack:

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.min:
            val = min(val,self.min[-1])
        self.min.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()