class Solution:
    
    # main idea:
    # binary_search method: O(lgn)
    
    def my_binary_search(self, nums, begin, end):
        
        # calculate 'mid'
        mid = (begin+end) // 2
        
        # This condition is needed to handle the case when array is not rotated at all
        if begin >= end:
            # return the 1st one
            return nums[0]   
        # Check if element 'mid+1' is minimum element
        elif nums[mid+1] < nums[mid]:
            return nums[mid+1]
        # Check if 'mid' itself is minimum element 
        elif nums[mid] < nums[mid-1]:
            return nums[mid]
        # Decide whether we need to go to left half or right half !!!
        elif nums[end] > nums[mid]:
            return self.my_binary_search(nums, begin, mid-1)
        else:
            return self.my_binary_search(nums, mid+1, end)
    
    def findMin(self, nums: List[int]) -> int:
        
        # special case        
        if len(nums)==1:
            return nums[0]
        
        # Find Minimum
        my_min = self.my_binary_search(nums, 0, len(nums)-1)
        return my_min
