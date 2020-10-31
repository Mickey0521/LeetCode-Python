class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        # main idea:
        # The Reverse Polish Notation (RPN) is also known as 
        # the 'postfix' notation, because each operator appears after its operands.
        # Stack fits perfectly as it is a Last-In-First-Out (LIFO) data structure.
        
        my_stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in operators:
                operand = int(token) # we need to change it to 'integer'
                my_stack.append(operand) # push
            else:
                a = my_stack.pop()
                b = my_stack.pop()
                # be careful: need to use 'b-a' and 'b//a'
                if token == '+':
                    c = b + a
                    my_stack.append(c)
                elif token == '-':
                    c = b - a
                    my_stack.append(c)
                elif token == '*':
                    c = b * a
                    my_stack.append(c)    
                else:
                    # special case (becasue Python is different from C language)
                    if b * a < 0: 
                        c = -((-b) // a)
                        my_stack.append(c) 
                    else:                    
                        c = b // a
                        my_stack.append(c)  
        
        final_value = my_stack.pop() # pop the final value in the stack
        return final_value
    
