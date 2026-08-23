# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: Optional[TreeNode]
        """
        # can jjust do recursion on tree, set left to result of recursive call
        # simple rule: if no child and val is target, return none
        # else return self
        if root == None:
            return None
        
        root.right = self.removeLeafNodes(root.right, target)
        root.left = self.removeLeafNodes(root.left, target)
        if root.left == None and root.right == None:
            return None if root.val == target else root
        return root
