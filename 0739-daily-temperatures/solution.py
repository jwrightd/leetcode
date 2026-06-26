class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #brute force is to start at i, iterate until you see something greater
        # can we use dp?
        # no, maybe monotonically decreasing stack
        # algo:
        # we take ith
        # if it is greater than top of stack, we pop until top off stack is < ith element or stack empty, i is index for all of those
        # if it is <= top of stack, we add it to top of stack
        #everything at the end after last element is processed is set to 0
        stk = []
        length = len(temperatures)
        output = [0 for i in range(length)]
        for idx in range(length):
            while stk and temperatures[stk[-1]] < temperatures[idx]:
                removedIdx = stk.pop(-1)
                output[removedIdx] = idx - removedIdx
            stk.append(idx)
        return output
        
