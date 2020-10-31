class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0
        
        # key point: use two pointers (left and right)
        left = 0
        right = 0
        
        # use dictionary (to store the index)
        dictionary = {}
        
        # keep moving the index (i.e., the right pointer)
        for index in range( len(s) ):
            
            right = index
            
            if s[right] not in dictionary:
                dictionary[ s[right] ] = right 
            else:
                # left = dictionary[ s[right] ] + 1   # update left
                
                # be careful: left must go ahead, cannot go back
                # so, we use 'max' to update left
                left = max(left, dictionary[ s[right] ] + 1)
                
                # update the dictionary
                dictionary[ s[right] ] = right
            
            # print(dictionary)
            # print(left)
            # print(right)
            max_len = max(max_len, right - left + 1)
        
        return max_len
