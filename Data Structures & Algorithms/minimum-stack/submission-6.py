class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            lst = [val, val]
            self.stack.append(lst)
        
        else:
            old_min = self.stack[-1][1]
            curr_min = min([val, old_min])
            self.stack.append([val, curr_min])
        
        return None
        

    def pop(self) -> None:
        self.stack.pop()
        return None
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]