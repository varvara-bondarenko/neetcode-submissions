class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_stack[-1]: 
            self.min_stack.append(val)

    def pop(self) -> None:
        top_el = self.stack.pop()
        if top_el == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        top_el = self.stack.pop()
        self.stack.append(top_el)
        return top_el

    def getMin(self) -> int:
        return self.min_stack[-1]
    