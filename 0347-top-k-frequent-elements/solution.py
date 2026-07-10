class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        heap = []
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        for i in freq:
            heapq.heappush(heap, (-freq[i], i))
        output = []
        for i in range(k):
            val, i = heapq.heappop(heap)
            output.append(i)
        return output

        
