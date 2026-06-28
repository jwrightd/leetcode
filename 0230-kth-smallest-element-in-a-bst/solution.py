# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # ideas: add everything to heapq and pop k
        # adding everything is o(n)
        # poppign k is o(Klogn)
        #so o(n) algorithm 

        # but maybe we can do this in klogn

        #inorder traversal is left root right
        #ohhh inorder gives us the node values (in order LOL)

        #maybe lets do like a counter
        visited = set()

        def inorder(root):
            if root == None:
                return None
            l = inorder(root.left)
            if l != None:
                return l
            visited.add(root.val)
            if len(visited) == k:
                return root.val
            
            r = inorder(root.right)
            if r != None:
                return r
            
        return inorder(root)

            

        
