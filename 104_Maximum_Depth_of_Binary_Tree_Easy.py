# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# define a method to find max_depth
def max_depth(root, current_depth):
    
    # the bottom
    if not root:
        return 0 
    
    # recursive (left and right)
    left_depth = max_depth(root.left, current_depth)
    right_depth = max_depth(root.right, current_depth)
    
    # max(left,right)+1
    current_depth = max( left_depth, right_depth ) + 1
    
    # return the depth
    return current_depth

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    
        # call max_depth
        return max_depth(root, 0)
