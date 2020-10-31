167. Two Sum II - Input array is sorted
Easy

1551

583

Add to List

Share
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

##########################################################################

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
                
##########################################################################

Success
Details 
Runtime: 56 ms, faster than 96.33% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.4 MB, less than 40.90% of Python3 online submissions for Two Sum II - Input array is sorted.

##########################################################################

# O(n) runtime, O(n) space - Hash table
we could reduce the runtime complexity of looking up a value to O(1) using a hash map 
that maps a value to its index

# O(n) runtime, O(1) space
Note that we may reduce the space complexity to O(1) using Two Pointers (i and j). 
Three possibilities:
Ai + Aj > target
Ai + Aj < target
Ai + Aj == target
