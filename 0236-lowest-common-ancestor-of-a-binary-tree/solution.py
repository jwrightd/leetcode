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
        # maybe we need to search for p, q, and then store the paths
        paths = {}
        def dfs(node, tgt, dirs):
            
            if node == None:
                return
            if node.val == tgt:
                paths[tgt] = [i for i in dirs]
                return 
            dirs.append(1)
            dfs(node.right, tgt, dirs)
            dirs.pop()
            dirs.append(0)
            dfs(node.left, tgt, dirs)
            dirs.pop()

        dfs(root, p.val, [])
        
        dfs(root, q.val, [])

        idx = 0
        lca = root
        while len(paths[p.val]) > idx and len(paths[q.val]) > idx and paths[p.val][idx] == paths[q.val][idx]:
            direction = paths[p.val][idx]
            if direction == 0:
                lca = lca.left
            else:
                lca = lca.right
            
            idx += 1

        return lca
        
            
            


        
