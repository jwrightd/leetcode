# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        minLev = -1
        minSum = float('inf')

        queue = []
        nextLvl = []
        queue.append(root)
        currSum = 0
        currLev = 1
        while queue or nextLvl:
           # print(queue, nextLvl)
            #print(currSum, currLev)
            if queue:
                curr = queue.pop()
                currSum += curr.val
                if curr.left != None:
                    nextLvl.append(curr.left)
                if curr.right != None:
                    nextLvl.append(curr.right)
            else:
                queue = [i for i in nextLvl]
                nextLvl = []
                
                if currSum < minSum:
                    minSum = currSum
                    minLev = currLev
                currLev += 1
                currSum = 0
        if currSum < minSum:
            minLev = currLev
        return minLev

            


        
