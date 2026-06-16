# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # max(maxPathSum on left, mPS on right, sum + mid)
        self.ans = float('-inf')
        def dfs(root):
            if root == None:
                return 0
            
            leftPath = max(0, dfs(root.left))
            rightPath = max(0, dfs(root.right))

            self.ans = max(self.ans, leftPath + rightPath + root.val)
            return root.val + max(leftPath, rightPath)

        dfs(root)
        return self.ans

        
