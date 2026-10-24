class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pairs = {}
        pairs["6"] = "9"
        pairs["9"] = "6"
        pairs["8"] = "8"
        pairs["1"] = "1"
        pairs["0"] = "0"
        res = []
        def dfs(l, r, state):
            if l > r:
                res.append("".join(state))
                return
            for nbr in ["6", "9", "8", "1", "0"]:
                if l == 0 and nbr == "0" and n != 1:
                    continue
                if l == r and nbr in ["6", "9"]:
                    continue
                state[l] = nbr
                state[r] = pairs[nbr]
                dfs(l + 1, r - 1, state)
                state[l] = -1
                state[r] = -1


        dfs(0, n - 1, [-1 for _ in range(n)])
        return res

        

