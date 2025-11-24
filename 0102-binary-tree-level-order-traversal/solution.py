# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        queue = []
        ret = []
        retDict = dict()
        queue.append((root, 0))
        maxLvl = 0
        while len(queue) > 0:
            tmp, lvl = queue.pop(0)
            maxLvl = lvl
            if lvl in retDict:
                retDict[lvl].append(tmp.val)
            else:
                retDict[lvl] = [tmp.val]
            if tmp.left != None:
                queue.append((tmp.left, lvl + 1))
            if tmp.right != None:
                queue.append((tmp.right, lvl + 1))
        for i in range(maxLvl + 1):
            ret.append(retDict[i])
        return ret
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
