class Solution:
    
    # main idea: dynamic programming (DP)
    # Besides keeping track of the largest product, 
    # we also need to keep track of the smallest product.
    # be careful: 'contiguous' subarray

    def my_product(self,nums):
        
        # special case
        if len(nums)==1:
            return nums[0]
        
        # initialization
        my_max = [0 for _ in range(len(nums))]
        my_min = [0 for _ in range(len(nums))]
        print(my_max)
        print(my_min)
        
        # set the base
        my_max[0] = nums[0]
        my_min[0] = nums[0]
        
        # need to initialize the 'final_max'
        final_max = nums[0]
        
        for i in range(1, len(nums)):
            # update 'max' and 'min'
            my_max[i] = max(my_max[i-1]*nums[i], my_min[i-1]*nums[i], nums[i])
            my_min[i] = min(my_max[i-1]*nums[i], my_min[i-1]*nums[i], nums[i])
            # need to update the 'final_max'
            final_max = max(final_max, my_max[i])
        
        return final_max
    
    def maxProduct(self, nums: List[int]) -> int:
        
        # test case
        #test_input = [-4,-3]
        #test_result = self.my_product(test_input)
        #print(test_result)
        
        result = self.my_product(nums)
        return result
