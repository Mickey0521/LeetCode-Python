# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def min_depth(root, current_depth):
    
    if not root:
        return 0
    
    ####################################################
    # Similar to the [Recursion] approach to find the maximum depth, 
    # but make sure you consider these cases:
    # Node that has one empty sub-tree while the other one is non-empty. 
    # Return the minimum depth of that non-empty sub-tree.
    if not root.left:
        return min_depth(root.right, current_depth) + 1;
    if not root.right:
        return min_depth(root.left, current_depth) + 1;
    ####################################################
    
    # recursive (left and right)
    left_depth = min_depth(root.left, current_depth)
    right_depth = min_depth(root.right, current_depth)
    current_depth = min( left_depth, right_depth) + 1
    
    return current_depth
    

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        return min_depth(root, 0)
