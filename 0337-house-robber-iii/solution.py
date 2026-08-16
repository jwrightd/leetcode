# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # so we skip choose current node and move to all children with valid take
        # or we rob current node and go to children with invalid
        # need to find some way to memo
        dp = {}
        def dfs(node, canRob):
            if node == None:
                return 0
            
            if (node, canRob) in dp:
                return dp[(node, canRob)]
            skip = dfs(node.left, True) + dfs(node.right, True)
            take = 0
            if canRob:
                take = node.val + dfs(node.left, False) + dfs(node.right, False)
            dp[(node, canRob)] = max(skip, take)
            return max(skip, take)
        return dfs(root, True)
                
        
