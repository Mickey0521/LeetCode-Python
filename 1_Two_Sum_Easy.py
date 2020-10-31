1. Two Sum
Easy

15021

543

Add to List

Share
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

############################################################

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

############################################################

Success
Details 
Runtime: 48 ms, faster than 79.68% of Python3 online submissions for Two Sum.
Memory Usage: 15.9 MB, less than 8.51% of Python3 online submissions for Two Sum.

############################################################

# O(n) runtime - Hash table
we could reduce the runtime complexity of looking up a value to O(1) using a hash map 
that maps a value to its index

