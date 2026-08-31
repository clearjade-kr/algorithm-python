class MinStack:

    def __init__(self):
        # min_stack will have (cur_stack_val, cur_min_val)
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append((val, val))
        else:
            self.min_stack.append((val, min(self.min_stack[-1][1], val)))

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]