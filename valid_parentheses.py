class Solution:
    def isValid(self, s: str) -> bool:
        
        # main idea:
        # A Last-In-First-Out (LIFO) data structure 
        # such as 'stack' is the perfect fit
        
        if len(s)==0:
            return True
        
        valid_char = ['(', ')', '{', '}', '[', ']']
        
        left_half = ['(', '[', '{']
        right_half = [')', ']', '}']
        
        # use a map/dictionary, which is more maintainable
        another_half = {')': '(', '}':'{', ']':'['}
        
        my_stack = []
        
        for char in s:
            if char not in valid_char:
                return False
            
            # we see an opening parenthesis, we push it onto the stack
            if char in left_half:
                my_stack.append(char)
            
            # we encounter a closing parenthesis, we pop the last inserted opening parenthesis
            if char in right_half:
                if len(my_stack) == 0:
                    return False
                # be careful: check if the pair is a valid match
                elif another_half[char] != my_stack[len(my_stack)-1]:
                    return False
                else:
                    my_stack.pop()
        
        if len(my_stack) !=0:
            return False
        else:
            return True
            
