151. Reverse Words in a String
Medium

965

2791

Add to List

Share
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

##########################################################################

class Solution:
    def reverseWords(self, s: str) -> str:
        
        # O(n) runtime, using two-pass solution
        
        # 1st pass, split the string by spaces into an array of words
        my_word_list = []
        my_word_list = s.split(" ") # str.split() will return a 'list'
        print(my_word_list)
        
        # important: 
        # use 'filter' to remove 'None' 
        # note: in python 3, filter() does not return a list, 
        # so we need to transfer it into 'list' by ourselves
        my_word_list = list( filter(None, my_word_list) )
        print(my_word_list)
        
        # 2nd pass, reverse the words
        # reverse a list by using 'list[::-1]'
        reverse_word_list = my_word_list[::-1]
        print(reverse_word_list)

        # transfer 'list' back to 'str'
        reverse_str = ''
        for item in reverse_word_list:
            reverse_str = reverse_str + ' ' + item
        
        # remove the 1st space
        reverse_str = reverse_str[1::]
        print(reverse_str)

        return reverse_str

##########################################################################

Success
Details 
Runtime: 28 ms, faster than 77.37% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.6 MB, less than 16.89% of Python3 online submissions for Reverse Words in a String.

##########################################################################

O(n) runtime - two-pass solution:

1. First pass to split the string by spaces (into an array of words)
2. Second pass to extract the words in reversed order
