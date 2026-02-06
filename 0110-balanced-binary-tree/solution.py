# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return True if root == None else (self.height(root.left) - self.height(root.right))**2**1/2 <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        return 1 + max(self.height(root.right), self.height(root.left)) if root !=  None else 0
        
