class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        heap = []
        size = 0
        for i in arr:
            
            heapq.heappush(heap, (-abs(i - x), -i))
            size += 1
            if size == k + 1:
                heapq.heappop(heap)
                size -= 1
        res = []
        while heap:
            dist, num = heapq.heappop(heap)
            res.append(-num)
        return sorted(res)
