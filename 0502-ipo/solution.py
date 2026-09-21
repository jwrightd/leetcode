class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # profit is what we get
        # capital is hwat we need
        # want to maximize profit, return final capital (init w + profit)
        # how do we solve ts
        # we can choose all projs for <= our cpaital
        # max heap with profit?
        # in theory you always want to pick the most profitable project giving your capital
        # bc you can have everything up to ur capital, makes sense to have heap. 
        # or maybe we just sort by capital?

        # ohshit i get it
        # ok first we make (profit, capital) objs
        # then we sort by capital
        # then we make our heap
        # for i in range k
        # while we can add valid things to our heap (where min cap <= what we have rn), we add
        # then the one we pop is optimal and we increment our capital

        # this hsould be nlogn total
        # worst case we do logn heappush n times and then heappop 3x

        import heapq

        heap = []
        N = len(profits)
        objects = []
        for _ in range(N):
            objects.append([profits[_], capital[_]])
        objects.sort(key = lambda x : x[1]) # sort on capital
        idx = 0
        for i in range(k):
            while idx < N and objects[idx][1] <= w:
                heapq.heappush(heap, [-objects[idx][0]])
                idx += 1
            if heap:
                w -= heapq.heappop(heap)[0]
        return w


        
