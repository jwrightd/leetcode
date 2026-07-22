class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        coordinates.sort() # need to sort
        slope = float(coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0]) if coordinates[1][0] != coordinates[0][0] else float('inf')
        intercept = coordinates[0][1] - coordinates[0][0] * slope if slope != float('inf') else 0
        #print(slope, intercept)
        for x, y in coordinates[2:]:
            if slope == float('inf'):
                if x != coordinates[0][0]:
                    return False
            else:
                if y != slope * x + intercept:
                    return False
        return True
        
