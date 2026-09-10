# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recur(root):
            if root == None:
                return (0,0,0)
            leftSum, leftNodes, tvl = recur(root.left)
            rightSum, rightNodes, tvr = recur(root.right)
            nv = 0
            if (leftSum + rightSum + root.val)//(leftNodes + rightNodes + 1) == root.val:
                nv += 1
            return (leftSum + rightSum + root.val, leftNodes + rightNodes + 1, nv + tvl + tvr)
        return recur(root)[2]

        
