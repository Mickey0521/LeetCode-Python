class MinStack:

    # main idea:
    # 1. Consider using an extra stack to keep track of the current minimum value. 
    # 2. During the push operation, 
    #    we choose the new element or the current minimum, 
    #    whichever that is smaller to push onto the min stack.
    # 3. For the pop operation, we would pop from both stacks.
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = [] # min_stack
        
    def top(self) -> int:
        my_top = self.stack_1[-1] # the last one of stack 1     
        return my_top

    def getMin(self) -> int:
        my_min = self.stack_2[-1] # the last one of stack 2    
        return my_min
    
    def pop(self) -> None:
        self.stack_1.pop()
        self.stack_2.pop()    
    
    def push(self, x: int) -> None:
        
        self.stack_1.append(x)
        
        # key point: 
        # push the current minimum ( x or self.stack_2[-1])
        if self.stack_2 == []:
            self.stack_2.append(x)
        elif (x < self.stack_2[-1]):
            self.stack_2.append(x)
        else:
            self.stack_2.append(self.stack_2[-1]) # push the current minimum

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
