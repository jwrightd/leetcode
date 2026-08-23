class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # seems to be graph problem with weights
        # can only go to a child greater than itself
        # have car with capacity seats at 0
        # maybe isnt a graph problem
        # just greedy, want to sort trips
        # keep running capacity count as we process 
        # oh wait no
        # lets do a heap, we subtract from capacity at from and then add it back at to
        # we just pop everything off (heap keyed by like distance, then val)
        # if our runninng count is ever sub 0 then return false
        import heapq
        heap = []
        for np, f, t in trips:
            heapq.heappush(heap, [f, t, -np])
            heapq.heappush(heap, [t, t, np])
        while heap:
            loc, start, val = heapq.heappop(heap)
            capacity += val
            if capacity < 0:
                return False
        return True


        
