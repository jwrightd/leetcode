# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        dummy = TreeNode(-1)
        dummy.left = root
        curr = root
        parent = dummy
        
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            
        if not curr: # Not found
            return root
        
        # 2 ch
        if curr.left and curr.right:
            # what node to replace with
            # either smallest in right subtree or biggest in left subtree
            biggest = curr.left
            bigParent = curr
            while biggest.right:
                bigParent = biggest
                biggest = biggest.right
            
            curr.val = biggest.val
            if bigParent.left == biggest: 
                bigParent.left = biggest.left
            else:
                bigParent.right = biggest.left


        
        else: # 0/1 ch
            # can connect like so
            child = curr.left if curr.left else curr.right
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        return dummy.left   

        
