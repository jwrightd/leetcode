# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # extend the paths down
        # recur
        self.high = 0
        def dfs(node, tot):
            if node == None:
                return
            self.high = max(self.high, tot)
            r, l = 0 ,0 
            if node.right:
                r = dfs(node.right, 1) if node.val != node.right.val - 1 else dfs(node.right, tot + 1)
            if node.left:
                l = dfs(node.left, 1) if node.val != node.left.val - 1 else dfs(node.left, tot + 1)
        dfs(root, 1)
        return self.high
