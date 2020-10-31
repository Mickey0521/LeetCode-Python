class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # brute force method: O(n)
        
        my_min = nums[0]    
        for num in nums:
            if num < my_min:
                my_min = num
        
        return my_min
