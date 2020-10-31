class Solution:   
    
    # main idea:
    # use 'binary_search' for a 'sorted array'
    # be careful: If not, return the index where it would be 'if it were inserted' in order
    
    def my_binary_search(self, nums, target, begin, end):
        
        # calculate the mid (by using 'plus')
        mid = (end + begin) // 2   
        print(mid)
        
        # set the 'stopping' condition
        if begin > end:
            # be careful: return the 'Insert Position' => return 'begin'
            return begin
        elif nums[mid] == target:
            return mid
        # the recursion of binary search
        elif nums[mid] < target:
            return self.my_binary_search(nums, target, mid+1, end)
        elif nums[mid] > target:
            return self.my_binary_search(nums, target, begin, mid-1)
        #else:
        #    return 0
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # return the 'index'
        index = self.my_binary_search(nums, target, 0, len(nums)-1)
        return index
