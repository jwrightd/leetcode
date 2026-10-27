class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        N = len(citations)
        # largest idx s.t citations[i] >= i
        #print(citations)
        for i in range(N):
            if citations[i] <= i:
                return i
        return N
        
