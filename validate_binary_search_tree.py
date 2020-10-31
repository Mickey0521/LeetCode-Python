# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# define a method to test if it is a BST
def BST_valid(root, min_value, max_value):
    
    # not a TreeNode
    if not root:
        return True
    
    # the cases: not a BST
    if (root.val >= max_value) or (root.val <= min_value):
        return False
    
    # test the left node
    left_test = BST_valid( root.left, min_value, root.val)
    # test the right node
    right_test = BST_valid( root.right, root.val, max_value)
    
    # return the result
    return (left_test and right_test)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # initialize the max and min values
        max_inf = float('inf')
        min_inf = float('-inf')

        # recursive test
        return BST_valid(root, min_inf, max_inf)
