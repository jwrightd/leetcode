# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: Optional[TreeNode]
        :type arr: List[int]
        :rtype: bool
        """
        N = len(arr)
        
        def dfs(i, node):      
            if node == None:
                return False
            
            if i == N - 1 and arr[i] == node.val and node.left == None and node.right == None:
                return True
            elif i == N or (node.left == None and node.right == None):
                return False
            if arr[i] != node.val:
                return False
            

            left = dfs(i + 1, node.left)
            right = dfs(i + 1, node.right)
            return left or right
        
        return dfs(0, root)
            

