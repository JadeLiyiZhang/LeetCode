class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        else:
            for i in range(len(self.queue_in) - 1):
                element = self.queue_in.popleft()
                self.queue_out.append(element)
            self.queue_in, self.queue_out = self.queue_out, self.queue_in
            return self.queue_out.popleft()
            

    def top(self) -> int:
        if self.empty():
            return None
        else:
            element = self.queue_in.pop()
            self.queue_in.append(element)
            return element

    def empty(self) -> bool:
        return len(self.queue_in) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()