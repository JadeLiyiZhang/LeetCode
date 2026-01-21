class MinStack:

    def __init__(self):
        self.minstack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        if not self.min_value:
            self.min_value.append(val)
        else:
            self.min_value.append(min(self.min_value[-1], val))

    def pop(self) -> None:
        self.minstack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()