# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def height(root):
            if root == None:
                return 0
            l = height(root.left)
            r = height(root.right)
            diam = l + r
            val = max(l, r)
            self.diameter = diam if diam > self.diameter else self.diameter
            return val + 1
        
        height(root)
        return self.diameter
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
    
        
        
