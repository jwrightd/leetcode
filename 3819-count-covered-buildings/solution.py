class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        xs = defaultdict(list)
        ys = defaultdict(list)

        for x, y in buildings:
            xs[x].append([y, x, y])
            ys[y].append([x, x, y])
        for x in xs:
            xs[x].sort()
        for y in ys:
            ys[y].sort()
        validX = set()
        count = 0
        validY = set()
        for i in xs:
            for q in range(1, len(xs[i]) - 1):
                a, b, c = xs[i][q]
                validX.add((b, c))
        for i in ys:
            for q in range(1, len(ys[i]) - 1):
                a, b, c = ys[i][q]
                validY.add((b, c))
        for i in validX:
            if i in validY:
                count += 1
        return count
