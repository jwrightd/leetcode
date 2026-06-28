# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #some recursion, we keep root same, swap left and right, and the invert both
        if root == None:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
