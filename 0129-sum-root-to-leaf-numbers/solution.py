# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # dfs str and then int cast and sum
        tot = 0
        val = [str(root.val)]
        
        def dfs(node):
            nonlocal tot
            if not node.left and not node.right:
                tot += int("".join(val))
                return
            if node.left:
                val.append(str(node.left.val))
                dfs(node.left)
                val.pop(-1)
            if node.right:
                val.append(str(node.right.val))
                dfs(node.right)
                val.pop(-1)
        
        dfs(root)
        
        return tot
        
