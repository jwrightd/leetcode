# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        # we can count, if
        dominants = []
        def recur(node):
            if node == None:
                return -1

            left = recur(node.left)
            right = recur(node.right)
            if node.val >= left and node.val >= right:
                dominants.append(node.val)

            return max([left, right, node.val])
        recur(root)
        return len(dominants)
