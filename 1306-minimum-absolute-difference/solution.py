class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        small = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            small = arr[i + 1] - arr[i] if arr[i + 1] - arr[i] < small else small
        ret = []
        arrSet = set(arr)
        for i in arr:
            if i + small in arrSet:
                ret.append([i, i + small])
        return ret
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
