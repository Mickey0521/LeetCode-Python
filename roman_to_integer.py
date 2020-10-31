class Solution:
    def romanToInt(self, s: str) -> int:
        
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
                     }
        
        my_sum = 0
        
        for i in range( len(s) ):            
            if i ==0:
                my_sum = dictionary[s[i]]
            elif dictionary[s[i-1]] < dictionary[s[i]]:
                # be careful:
                # smaller roman literal ‘I’ appears before it, 
                # we need to subtract ‘I’ from ‘V’
                # that we already added another ‘I’ before it, 
                # so we need to subtract a total of 'two' one’s from it
                my_sum = my_sum + dictionary[s[i]] - (2*dictionary[s[i-1]])
            else:
                my_sum = my_sum + dictionary[s[i]]
        
        return my_sum
