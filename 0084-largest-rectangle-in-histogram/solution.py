class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #some stack problem
        #Lets think about this, 
        #largest histogram at index is is heights[i] * (right - left -  1), where right and left are the closest indices that are lss than heights[i]

        #so we want to go one by one and do this, the histograms cannot overlap, so we can use a stack

        # algo:
        # push indices to stack until you get something lower than the previous height
        # pop until the top of stack is less than or equal to your next height
        heights.append(0)
        stk = []
        maxArea = 0
        for idx, val in enumerate(heights):
            if len(stk) == 0:
                stk.append(idx)
            elif val >= heights[stk[-1]]:
                stk.append(idx)
            else:
                while len(stk) > 0 and val < heights[stk[-1]]:
                    ind = stk.pop()
                    width = idx - stk[-1] - 1 if len(stk) > 0 else idx
                    maxArea = maxArea if width * heights[ind] < maxArea else width * heights[ind]
                
                stk.append(idx)
        return maxArea
