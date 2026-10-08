class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.stack.append((val, self.min_val))
            self.min_val = val
        else:
            self.stack.append((val, None))

    def pop(self) -> None:
        val, prev_min = self.stack.pop()

        if prev_min is not None:
            self.min_val = prev_min

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_val