class MinStack:

    def __init__(self):
        self.stack = []; # just initializing the array.

    def push(self, val: int) -> None:
        self.stack = [val] + self.stack;
        
    def pop(self) -> None:
        self.stack = self.stack[1:];
    def top(self) -> int:
        return self.stack[0];
    def getMin(self) -> int:
        return min(self.stack);

        
