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
