class DetectSquares(object):

    def __init__(self):
        self.points = []
        self.ptdict = dict()

    def add(self, point):
        self.points.append(point)
        self.ptdict[(point[0], point[1])] = 1 if (point[0], point[1]) not in self.ptdict else 1 + self.ptdict[(point[0], point[1])]
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        #how do we detect a square here
        # check for points with same x, we need to check all points with same x, and all points with same y

        #then we see if the complete the square pt is available
        sameX = [i[1] for i in self.points if i[0] == point[0]]
        sameY = [i[0] for i in self.points if i[1] == point[1]]

        validSq = 0

        for i in sameX:
            for j in sameY:
                if (point[0] - j == point[1] - i or point[0] - j == - point[1] + i) and point[0] - j != 0 and (j, i) in self.ptdict:
                    validSq += self.ptdict[(j,i)]
        return validSq

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
