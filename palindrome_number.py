class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        my_str = str(x)
        
        # If the number is the same as its reversed,
        # then it must be a palindrome
        if my_str == my_str[::-1]:
            return True
        else:
            return False
        
