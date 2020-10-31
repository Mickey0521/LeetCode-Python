class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # simple solution: using 'brute force'
        # time compexity: O(n^3)
    
        # just check if string == reverse(string)
        def is_palindrome(my_str):
            if my_str == my_str[::-1]:
                return True
            else:
                return False
        
        # using two for-loop: 'brute force' (i and j)
        longest_palindrome = ''       
        for i in range( len(s) ):
            for j in range( i, len(s) ):
                
                # note that s[i:j+1] does not include s[j+1] (be super careful in Python)
                if is_palindrome( s[i:j+1] ):
                    
                    # keep the maximum
                    if len(s[i:j+1]) >= len(longest_palindrome):
                        longest_palindrome = s[i:j+1]
        
        return longest_palindrome
