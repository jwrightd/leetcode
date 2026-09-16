# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        valid = []
        if root == None:
            return []
        def dfs(node, total, path):
            if node.left == None and node.right == None:
                if total == targetSum:
                    valid.append([i for i in path])
                return
            if node.left != None:
                path.append(node.left.val)
                dfs(node.left, total + node.left.val, path)
                path.pop(-1)
            if node.right != None:
                path.append(node.right.val)
                dfs(node.right, total + node.right.val, path)
                path.pop(-1)
        dfs(root, root.val, [root.val])
        return valid
