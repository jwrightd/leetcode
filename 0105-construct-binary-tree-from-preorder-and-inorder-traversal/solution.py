# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # unique vals
        # preorder --> Root, Left, Right
        # inorder --> Left, Root, Right
        # first in preorder is always 
        # so we want to put our root, then find number of nodes to send left, find number to send right, recur on both
        preToin = {}
        for idx, val in enumerate(inorder):
            preToin[val] = idx
        n = len(preorder)

        def recur(preL, preR, inL, inR):
            if preL > preR:
                return None

            node = TreeNode(preorder[preL])
            mid = preToin[preorder[preL]]
            left = mid - inL
            node.left = recur(preL + 1, preL + left, inL, mid)
            node.right = recur(preL + mid - inL + 1, preR, mid + 1, inR)

            return node

        



            
        
            
        
        return recur(0, n - 1, 0, n - 1)


        
