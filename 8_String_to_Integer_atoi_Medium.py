8. String to Integer (atoi)
Medium

1517

8979

Add to List

Share
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

##########################################################################

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

##########################################################################

Success
Details 
Runtime: 44 ms, faster than 14.53% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 5.23% of Python3 online submissions for String to Integer (atoi).

##########################################################################

