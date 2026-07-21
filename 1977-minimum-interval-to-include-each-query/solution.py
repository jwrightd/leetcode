class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        
        # brute force:
        # sort intervals
        # for all queries
        # check smallest interval that contains
        # o(N*Q)
        # can we get like nlogn
        # heap approach?
        queryIdx = defaultdict(list)
        for idx, val in enumerate(queries):
            queryIdx[val].append(idx)
        queries.sort()
        intervals.sort()
        n = len(intervals)
        output = [-1] * len(queries)
        
        heap = []
        idx = 0
        for q in queries:
            while idx < n and intervals[idx][0] <= q:
                heapq.heappush(heap, (intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1])) # (width, r)
                idx += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap) # while the right value is < q
            output[queryIdx[q][0]] = heap[0][0] if heap else -1
            queryIdx[q].pop(0)
        return output
