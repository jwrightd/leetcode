class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        # im thinking color dict
        # color to freq
        # when we process new ball, if its new in the dict or freq is 0, then we inc color count
        # if our current color has exacly 1 occurrence, we subtract 1 and then add to dict (can either be +0 or + 1)
        
        # so we need color -> freq
        # and we need array of balls with colors so we can access curr color

        balls = {} # ball array
        colors = {}
        
        output = []
        numColors = 0


        for idx, color in queries:
            prevColor = 0 if idx not in balls else balls[idx]
            if prevColor != 0 and prevColor in colors:
                colors[prevColor] -= 1
                if colors[prevColor] == 0:
                    numColors -= 1
            if color not in colors or colors[color] == 0:
                colors[color] = 1
                numColors += 1
            else:
                colors[color] += 1
            balls[idx] = color
            output.append(numColors)
        return output




            

