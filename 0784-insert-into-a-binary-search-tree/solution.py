# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        parent = None
        curr = root
        while curr != None:
            parent = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        if parent == None:
            return TreeNode(val)
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root

        
