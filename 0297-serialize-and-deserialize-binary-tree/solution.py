# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if root == None:
            return ""
        output = []
        def dfs(root):
            if root == None:
                output.append("L") # LEAF
                return
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(output)

        # need way of encoding tree, makes sense to do DFS
        # [1, 2, L, L, 3, 4, L, L, 5, L, L]

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        vals = data.split(",")
        N = len(vals)
        if N == 0:
            return None
        i = 0
        root = TreeNode(-1)
        def dfs(node):
            nonlocal i
            if i == N or vals[i] == "L": # end or leaf
                i += 1
                return None
            node.val = vals[i]
            i += 1
            leftNode = dfs(TreeNode(-1))
            rightNode = dfs(TreeNode(-1))
            node.left = leftNode
            node.right = rightNode
            return node
        return dfs(root)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
