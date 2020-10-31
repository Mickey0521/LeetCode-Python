class Solution:
    def myAtoi(self, str: str) -> int:
        
        # The heart of this problem is dealing with 'overflow'
        
        # define int_max, int_min, and the sign (i.e., 1 and -1)
        int_max = 2147483648 - 1
        int_min = -2147483648
        sign = 1
        
        # edge case: empty string
        if str == '':
            return 0
        
        # skip whitespace(s)
        i = 0 
        # while (str[i]==' ') and (i<len(str)):
        while (i<len(str)) and (str[i]==' '):
            i += 1
        
        # be careful: must check if 'i < len(str)'
        if i<len(str):
            if (str[i]=='-'):
                sign = -1
                i += 1
            elif (str[i]=='+'):
                sign = 1
                i += 1
        
        # check if 'str[i].isdigit()'
        # then, check if 'my_digit * 10 will overflow'
        # my_digit *= 10
        # my_digit += current_digit
        # fianlly, return 'sign * my_digit'
        my_digit = 0
        # while (str[i].isdigit()) and (i<len(str)):
        while (i<len(str)) and (str[i].isdigit()):
        
            if my_digit * 10 <= int_max:
                my_digit = my_digit * 10
            else:
                if sign == 1:
                    return int_max
                elif sign == -1:
                    return int_min
            
            current_digit = int(str[i])
            if my_digit + current_digit <= int_max:
                my_digit = my_digit + current_digit
            else:
                if sign == 1:
                    return int_max
                elif sign == -1:
                    return int_min            
            
            # remember to plus one
            i += 1

        return sign * my_digit
