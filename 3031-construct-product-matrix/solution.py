class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # like precompute array except self
        # need suffix and prefix arr
        # oh we can just lke flatten it
        # and then we get this same thing again
        flattened = []
        M = len(grid)
        N = len(grid[0])
        MOD = 12345
        for i in range(M):
            for j in range(N):
                flattened.append(grid[i][j])
        
        prefix = [1 for _ in range(M * N)] # define prefix[i] as the product of all nums before i
        suffix = [1 for _ in range(M * N)] # define suffix[i] as product of all nums before i


        for i in range(1, M * N):
            prefix[i] = (prefix[i - 1] * flattened[i - 1]) % MOD
        for i in range(M*N - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * flattened[i + 1]) % MOD
        flat_pmat = [(prefix[i] * suffix[i]) % MOD for i in range(M * N)]
        p = [[0 for _ in range(N)] for _ in range(M)]
        count = 0
        i = 0
        j = 0
        while count < M * N:
            p[i][j] = flat_pmat[count]
            j += 1
            if j == N:
                j = 0
                i += 1
            count += 1
        return p
