class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        # sum must be a square
        # and must be able to make 4 sticks of length n
        tot = sum(matchsticks)
        desired = tot//4
        if tot % 4 != 0:
            return False
        # need to match big and small
        sizes = [desired, desired, desired, desired]
        matchsticks.sort(reverse=True)
        if matchsticks[0] > desired:
            return False
        N = len(matchsticks)

        def dfs(i):
            if i == N:
                return True

            for idx in range(4):
                if sizes[idx] - matchsticks[i] < 0:
                    continue
                sizes[idx] -= matchsticks[i]
                if dfs(i + 1):
                    return True
                sizes[idx] += matchsticks[i]

            return False
        return dfs(0)


        
