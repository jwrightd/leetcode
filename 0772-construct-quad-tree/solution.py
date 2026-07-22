"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        root = Node()
        def recur(node, i, j, y, x): # top left, then bottom right
            # check four corners
            # if all are same, return
            # else recur
            if y - i == 1 and x - j == 1:
                node.val = grid[i][j]
                node.isLeaf = 1

            else:
                node.val = 1
                node.isLeaf = 0
                node.topLeft = recur(Node(), i, j, (i + y) // 2, (j + x) // 2)
                node.topRight = recur(Node(), i, (j + x) // 2, (y + i) // 2, x)
                node.bottomLeft = recur(Node(), (i + y) // 2, j, y, (j + x) // 2)
                node.bottomRight = recur(Node(), (i +  y)// 2,(j + x)//2, y, x)
                if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf and node.topLeft.val ==  node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                    node.val = node.topLeft.val
                    node.isLeaf = 1
                    node.topLeft = None
                    node.bottomLeft = None
                    node.bottomRight = None
                    node.topRight = None


            return node
        recur(root, 0, 0, n, n)
        return root
        
