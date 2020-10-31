28. Implement strStr()
Easy

1489

1840

Add to List

Share
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

##########################################################################

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # be careful: the edge cases
        # what if haystack is empty? and what if needle is empty?
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 and len(needle) != 0:
            return -1
        
        # O(mn), Brute Force
        # it is sufficient to solve it using the most direct method
        # be careful: need to 'plus one for the 1st loop'!!
        # for index in range( len(haystack) - len(needle)):
        for index in range( len(haystack) - len(needle) + 1):
            for j in range( len(needle) ):
                if haystack[index+j] == needle[j]:
                    pass
                else:
                    break
                # the occurence of needle!!! (without a break)
                if j == (len(needle) -1):
                    return index

        # no occurence of needle, return -1
        return -1

##########################################################################

Success
Details 
Runtime: 32 ms, faster than 58.59% of Python3 online submissions for Implement strStr().
Memory Usage: 13.8 MB, less than 95.01% of Python3 online submissions for Implement strStr().

##########################################################################

O(mn) runtime - Brute Force:
It is sufficient to solve it using the most direct method.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
