class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # many sets of updates, just like run sum it
        arr = [0 for i in range(length)]
        update = [0 for i in range(length)]
        for start, end, inc in updates:
            update[start] += inc
            if end + 1 < length:
                update[end + 1] -= inc
        runSum = 0
        for i in range(length):
            runSum += update[i]
            arr[i] = runSum
        return arr
