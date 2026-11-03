# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # recursive unwinding
        # need to pass num of valid nodes up
        self.biggest = 0
        def dfs(node):
            if node == None:
                return (True, 0, float('inf'), float('-inf'))

            # valid, size, min, max
            
            leftValid, leftSize, leftMin, leftMax = dfs(node.left)
            rightValid, rightSize, rightMin, rightMax = dfs(node.right)

            if leftValid and rightValid and leftMax < node.val < rightMin:
                validSize = 1 + leftSize + rightSize
                self.biggest = max(self.biggest, validSize)
                return (True, validSize, min(leftMin, node.val), max(rightMax, node.val))

            return (False, 0, 0, 0)
        
        dfs(root)
        return self.biggest





        
