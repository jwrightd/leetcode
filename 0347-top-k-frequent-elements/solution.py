class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #better than nlogn --> so we use pq i think
        #heapify in n
        #we pop k, so thats klogn, and n + klogn is less than nlogn
        import heapq
        #setup dict o(N)
        freq = dict()
        for i in nums:
            freq[i] = 1 if i not in freq else freq[i] + 1
        num_freqs = [(-freq[i], i) for i in freq]

        heapq.heapify(num_freqs)

        output = []
        for i in range(k):
            frequency, val = heapq.heappop(num_freqs)
            output.append(val)
        return output
        
