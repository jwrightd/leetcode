# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root == None:
            return root == subRoot
        return self.recur(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
    def recur(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        elif root == None or subRoot == None:
            #print(root, subRoot)
            return False
        elif root.val != subRoot.val:
            #print(root.val, subRoot.val)
            return False
        l = self.recur(root.left, subRoot.left)
        r = self.recur(root.right, subRoot.right)
        return l and r
        
