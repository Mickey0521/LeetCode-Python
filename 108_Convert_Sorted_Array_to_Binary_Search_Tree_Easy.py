# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # key: pick the middle element from the sorted array in each iteration
    # using the divide and conquer methodology (binary search algorithm)
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        start = 0
        end = len(nums)-1
        tree = self.get_BST_node_from_array(nums, start, end)
        print(tree)
        return tree

    def get_BST_node_from_array(self, nums, start, end):
        
        # important: be careful
        if start > end:
            return None
        
        # key: calculate the 'mid'
        mid = (start+end) // 2
        
        # recursive method (note: using 'mid-1' for the left, and 'mid+1' for the right)
        node = TreeNode(nums[mid])
        node.left = self.get_BST_node_from_array(nums, start, mid-1)
        node.right = self.get_BST_node_from_array(nums, mid+1, end)
        
        return node
