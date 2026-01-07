class Solution(object):
    def orangesRotting(self, grid):
        newGrid = []
        orange_count = 0
        count = 0
        rotten = set()
        for i in grid:
            for x in i:
                newGrid.append(x)
                if x != 0:
                    orange_count += 1
                if x == 2:
                    rotten.add(count)
                count += 1
        #BFS
        turns = 0
        while len(rotten) != orange_count:
            toAdd = set()
            adds = 0
            for i in rotten:
                surrounding = self.childIdx(i, len(grid), len(grid[0]))
                for s in surrounding:
                    if newGrid[s] == 1:
                        newGrid[s] = 2
                        adds += 1
                        toAdd.add(s)
            if adds == 0:
                return -1
            turns += 1
            for i in toAdd:
                rotten.add(i)
        return turns
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    def childIdx(self, current, m, n):
        ret = []
        if current % n != 0:
            ret.append(current - 1)
        if (current + 1) % n != 0:
            ret.append(current + 1)
        if current - n >= 0:
            ret.append(current - n)
        if current + n < m * n:
            ret.append(current + n)
        return ret

        
