# can pass most of the normal cases
# but, cannot pass the special cases, such as "2e0"

class Solution:
    
    def isNumber(self, s: str) -> bool:
        
		# important: use the method str.strip() 
		# to handle the 'heading and trailing whitespace'
        ##################
        my_test_str = '3.'
        print(my_test_str)
        my_test_str = my_test_str.strip() #trim
        # my_test_str = my_test_str.lstrip() #ltrim (left)
        # my_test_str = my_test_str.rstrip() #rtrim (right)
        print(my_test_str)
        ##################
        
        my_s = s.strip()

		# without heading and trailing whitespace, then ...
        if my_s == '': 
            return False
        if my_s == '.':
            return False
        
		# handle the sign 
        i = 0    
        if my_s[i]=='+' or my_s[i]=='-':
            i += 1

        #print(i)
        #print(my_str[i:])
        
		# check if the string is a valid number or not
        my_s_is_valid_number = False
        while i < len(my_s): 
            if my_s[i].isdigit() == True:
                my_s_is_valid_number = True
                i +=1
            elif my_s[i] == '.':
                my_s_is_valid_number = True
                i += 1
                
                if i == len(my_s):
                    return True
                
				# the second loop: to check the chars after '.'
                while i < len(s): 
                    if my_s[i].isdigit() == True:
                        my_s_is_valid_number = True
                        i +=1
                    else:
                        return False
            else:
                return False
        
		# final return
        return my_s_is_valid_number
            
