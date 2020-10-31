class Solution:
    def reverse(self, x: int) -> int:
        
        # handle the sign (before reverse)
        sign = 0
        if x < 0:
            sign = -1
            x = -x # note: we keep the digits
        else:
            sign = 1
        
        # by using 'str' in Python
        my_str = str(x)
        # reverse string
        my_str = my_str[::-1] 
        
        # using lstrip() to remove '0' on the 'left' side  
        my_str = my_str.lstrip('0')
        ###############################
        # test_str = '12000'
        # test_str = test_str[::-1] 
        # test_str = test_str.lstrip('0') 
        # print(test_str)
        ###############################

        # be careful (after using strip)
        # special case (e.g., '0000000')
        if my_str == '':
            return 0
        
        # handle the sign (after reverse)
        if sign == -1:
            my_str = '-' + my_str
        
        # by using 'int' in Python
        my_integer = int(my_str)
        
        # handle the 'overflow/underflow' problems
        # note: the power operator in Python is **
        max_int = (2 ** 31) -1
        print(max_int)
        min_int = -(max_int +1)
        print(min_int)
        
        # handle the 'overflow/underflow' cases
        if (my_integer < min_int) or (my_integer > max_int):
            return 0
        
        return my_integer
        
