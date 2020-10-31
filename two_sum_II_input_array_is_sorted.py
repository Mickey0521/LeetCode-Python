class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # build a hash table (by using dictionary)
        my_dict = {}
        for index in range( len(numbers) ):
            my_dict[ numbers[index] ] = index
        
        # find the complementary number (and its index)
        for index in range( len(numbers) ):
            my_target = target - numbers[index]
            if my_target in my_dict:
                # note: you may not use the same element twice
                if index == my_dict[my_target]:
                    pass
                # note: both index1 and index2 are not zero-based.
                else:
                    # return [index, my_dict[my_target] ]
                    return [index+1, my_dict[my_target]+1 ]
                    # be careful: we need to plus '1' because they are 'not' zero-based!!
