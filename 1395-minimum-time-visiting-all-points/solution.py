class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # just greedy algo
        # go point by point
        # if x and y greater than current coords, then go diag2
        startX, startY = points[0]
        time = 0
        for x, y in points[1:]:
            #print(x, y)
            while x != startX or y != startY:
                #print(startX, startY)
                if startX == x:
                    startY = startY + 1 if y > startY else startY - 1
                elif startY == y:
                    startX = startX + 1 if x > startX else startX - 1
                else: # both diff
                    startY = startY + 1 if y > startY else startY - 1
                    startX = startX + 1 if x > startX else startX - 1       
                time += 1
            #print("done", startX, startY)
        return time
                
