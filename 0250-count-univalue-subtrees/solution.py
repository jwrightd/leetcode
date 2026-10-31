# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(root):
            # 1 if left and right are unival and root = L = R
            if root == None:
                return 0,0

            left, leftNodes = helper(root.left)
            right, rightNodes = helper(root.right)
            current = 0
            if left == leftNodes and right == rightNodes:
                if (root.left != None and root.left.val != root.val) or (root.right != None and root.right.val != root.val):
                    current = 0
                else:
                    current = 1

            return left + right + current, leftNodes + rightNodes + 1
        return helper(root)[0]
        
