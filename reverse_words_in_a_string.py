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
