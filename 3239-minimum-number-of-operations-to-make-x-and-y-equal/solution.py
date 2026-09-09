class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # just bfs?
        def children(num):
            res = [num - 1, num + 1]
            if num % 11 == 0:
                res.append(num // 11)
            if num % 5 == 0:
                res.append(num // 5)
            return res
        
        q = []
        q.append([x, 0])
        visited = set()
        while q:
            num, ops = q.pop(0)
            if num in visited:
                continue
            visited.add(num)
            if num == y:
                return ops
            for child in children(num):
                q.append([child, ops + 1])

