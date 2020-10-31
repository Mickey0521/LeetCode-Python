# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# get the depth (by using a recursive method)
def getDepth(root):
    if root == None:
        return 0
    else:
        # remember to add '1'
        return max(getDepth(root.left), getDepth(root.right)) + 1

class Solution:      
    def isBalanced( self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        # calculate the difference
        if abs( getDepth(root.left) - getDepth(root.right) ) > 1:
            return False
        # check the subtree (by using a recursive method)
        else:
            return ( self.isBalanced(root.left) and self.isBalanced(root.right) )
