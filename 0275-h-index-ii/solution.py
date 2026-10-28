class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # just bin search it
        # valid when N - mid + 1 >= citations[mid]
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = (low + high)//2
            if citations[mid] == N - mid:
                return citations[mid]
            if N - mid > citations[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return N - low

