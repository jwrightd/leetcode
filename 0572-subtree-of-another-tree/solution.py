# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # either root can be subtree, left can be St, or right can be St
        def validNode(node, subtree):
            if node == None and subtree == None:
                return True
            
            if (node == None and subtree != None) or (node != None and subtree == None) or node.val != subtree.val:
                return False
            
            
            return validNode(node.left, subtree.left) and validNode(node.right, subtree.right)
        
        if validNode(root, subRoot):
            return True 
        if root.left and self.isSubtree(root.left, subRoot) or root.right and self.isSubtree(root.right, subRoot):
            return True
        return False
        
