# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        return self.recur(root, root.val)
    def recur(self, root, greatest):
        if root == None:
            return 0
        goodNode = 1 if root.val >= greatest else 0
        nextGreatest = root.val if goodNode == 1 else greatest
        return goodNode + self.recur(root.left, nextGreatest) + self.recur(root.right, nextGreatest)
        
