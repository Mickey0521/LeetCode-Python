class Solution:
    
    # Brute Force method (will be out of time!)
    # be careful: 'contiguous' subarray
    
    def my_product(self,nums):
        
        if len(nums)==1:
            return nums[0]
        
        my_max = nums[0]
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i==j:
                    product = nums[j] 
                    # reset (because we try to find the 'contiguous' subarray)
                if i!=j:
                    # based on the previous product (because we try to find the 'contiguous' subarray)
                    product = product * nums[j] 
                my_max = max(my_max, product)
        
        return my_max
    
    def maxProduct(self, nums: List[int]) -> int:
        
        #test_input = [-4,-3]
        #test_result = self.my_product(test_input)
        #print(test_result)
        
        result = self.my_product(nums)
        return result
        
