# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []
        # do level order
        # for each level, just process it right to left, add the first node you see
        # return list

        output = []

        queue = []
        queue.append((root, 0))
        
        while queue:
            current, level = queue.pop(0)
            if len(output) <= level:
                output.append(current.val)
            if current.right != None:
                queue.append((current.right, level + 1))
            if current.left != None:
                queue.append((current.left, level + 1))
        return output

