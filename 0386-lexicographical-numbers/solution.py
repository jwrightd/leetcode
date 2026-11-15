class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # just backtrack soln ig?
        tgt = list(str(n))
        valid = []
        def dfs(val):
            if len(val) > len(tgt) or (len(val) == len(tgt) and val > tgt):
                return
            valid.append(int("".join(val)))
            for nbr in range(10):
                val.append(str(nbr))
                dfs(val)
                val.pop(-1)


            return

        for i in range(1, 10):
            dfs([str(i)])
        return valid
