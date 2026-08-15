# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        order = []
        def traversal(node):
            if node == None:
                return

            order.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return order
        
