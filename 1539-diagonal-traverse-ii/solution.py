class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # just go down and then right
        diags = {}
        for i, arr in enumerate(nums):
            for j, val in enumerate(arr):
                if i + j in diags:
                    diags[i + j].append(val)
                else:
                    diags[i + j] = [val]
        output = []
        for i in range(len(diags)):
            count = len(diags[i]) - 1
            while count >= 0:
                output.append(diags[i][count])
                count -= 1
        return output
