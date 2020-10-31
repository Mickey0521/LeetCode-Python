class Solution:
    def intToRoman(self, num: int) -> str:
        
        int_symbol = [1, 5, 10, 50, 100, 500, 1000]
        roman_symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        # key point: add the symbols of '4' and '9'
        int_symbol_v2 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_symbol_v2 = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        
        my_string = ''
        my_num = num
        
        # from largest to smallest
        '''
        Input: num = 58
        Output: "LVIII"
        Explanation: L = 50, V = 5, III = 3.
        '''
        for i in range( len(int_symbol_v2)-1, -1, -1 ):
            while my_num >= int_symbol_v2[i]:
                my_num = my_num - int_symbol_v2[i]
                my_string = my_string + roman_symbol_v2[i]
        
        return my_string
