# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # helper w traverse node and current root
        arr = []

        def traversal(root):
            # root left right
            if root == None:
                return None
            arr.append(root)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        N = len(arr)
        for idx in range(N - 1):
            arr[idx].right = arr[idx + 1]
            arr[idx].left = None
        

