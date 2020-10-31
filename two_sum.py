class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # build a hashtable (by using dictionary)
        # note: just store the index (because we need to return the indices)
        my_dict = {}
        for index in range( len(nums) ):
            my_dict[ nums[index] ] = index
        print(my_dict)
        
        # note: my_target is the complementary number
        # just check out if my_target is in the dictionary!!
        for index in range( len(nums) ):
            my_target = target - nums[index]
            if my_target in my_dict:
                # be careful: you may not use the same element twice!!! 
                if index == my_dict[my_target]:
                    pass
                else:             
                    return [index, my_dict[my_target] ]
