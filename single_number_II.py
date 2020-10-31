class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # using dictionary to count 'the number of times an element appears'
        dictionary = {}
        
        # 1st run
        for item in nums:
            if item not in dictionary:
                dictionary[item] = 1
            else:
                dictionary[item] += 1
        
        # 2nd run
        for item in dictionary:
            if dictionary[item] == 1:
                return item
