class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # plus one
        carry_digit = 0
        digits[len(digits)-1] = digits[len(digits)-1] + 1
        
        # for loop (start from the last one)
        for index in range( len(digits)-1, -1, -1):
            
            # add the carry_digit
            digits[index] = digits[index] + carry_digit
            
            if digits[index] == 10:
                digits[index] = 0
                carry_digit = 1
            else:
                digits[index] = digits[index]
                carry_digit = 0

        # handle the edge case: 
        # append integer to the beginning of the list 
        if carry_digit == 1:
            digits.insert(0, 1) # insert(index, value)
                
        return digits
