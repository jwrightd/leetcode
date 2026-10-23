class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        valid = []
        qset = set()
        for x,y in queens:
            qset.add((x,y))
        # just check all 8 directions and you eihter run into a queen or a wall
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for i, j in directions:
            kx, ky = king
            while 0 <= kx < 8 and 0 <= ky < 8:
                if (kx, ky) in qset:
                    valid.append([kx, ky])
                    break
                kx += i
                ky += j
        return valid
                

