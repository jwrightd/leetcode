# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #do BST search for both
        #for a node n:
        # if p is in left and q is in right OR p/q is in n, then n is LCA

        #oh, because we have BST, our root val must not be greater than or less than both values
        #so we do dfs, if our node has the above condition then we have found it and we return all the way
        def dfs(node):
            if node == None:
                return None
 
            if not ((node.val > p.val and node.val > q.val) or (node.val < p.val and node.val < q.val)):
                return node
            
            if node.val > p.val and node.val > q.val:
                res = dfs(node.left)
            else:
                res = dfs(node.right)
            if res != None:
                return res
            return None
        
        return dfs(root)
        

        
