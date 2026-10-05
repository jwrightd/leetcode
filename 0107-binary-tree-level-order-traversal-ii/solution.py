# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        # just do normal level order w q then reverse
        traversal = defaultdict(list)
        depth = 0
        queue = [[root, 0]]
        while queue:
            curr, lvl = queue.pop(0)
            depth = lvl
            if curr.left != None:
                queue.append([curr.left, lvl + 1])
            if curr.right != None:
                queue.append([curr.right, lvl + 1])
            traversal[lvl].append(curr.val)
        
        ret = []
        while depth >= 0:
            ret.append(traversal[depth])
            depth -= 1
        return ret
        

        
