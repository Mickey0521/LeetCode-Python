125. Valid Palindrome
Easy

1124

2806

Add to List

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

##########################################################################

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 1st loop: build my_str only with 'alpha' and 'num' (skip other characters)
        # note: 'alphanumeric' means 'alpha' and 'num'
        my_str = []
        for char in s:
            if char.isalpha() or char.isalnum():
                my_str.append(char)
        print(my_str)
        
        # important: 
        # if my_str is an 'empty string' is also a valid palindrome
        if len(my_str) == 0:
            return True
        
        # O(n), using two pointers (head and tail)
        left_pointer = 0
        right_pointer = len(my_str) - 1
        
        # note: the condition is 'left < right'
        while left_pointer < right_pointer:
            if my_str[left_pointer].lower() == my_str[right_pointer].lower():
                pass
            else:
                return False
            left_pointer += 1
            right_pointer -= 1
        # be careful: ignoring cases, so we use '.lower()'
        
        return True

##########################################################################

Success
Details 
Runtime: 56 ms, faster than 38.85% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15 MB, less than 28.98% of Python3 online submissions for Valid Palindrome.

##########################################################################

# note: what about an empty string? 
empty string is a valid palindrome.

# O(n) runtime
The idea is simpe, use two pointers (head and tail).
