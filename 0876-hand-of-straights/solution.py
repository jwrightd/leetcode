class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        # ok we use heap i think

        #first we see if it is possible by N and groupsize
        n = len(hand)
        if n % groupSize != 0:
            return False

        import heapq

        heap = []

        for num in hand:
            heapq.heappush(heap, num)
        #now we pop in sets of groupSize, and we need n unique

        while heap:
            current = []
            currSet = set()
            addBack = []

            while heap and len(current) != groupSize:
                num = heapq.heappop(heap)
                if num not in currSet:
                    currSet.add(num)
                    current.append(num)
                else:
                    addBack.append(num)
            
            if len(current) != groupSize:
                return False
            
            for i in range(1, groupSize):
                if current[i] != current[i - 1] + 1:
                    return False
            
            for num in addBack:
                heapq.heappush(heap, num)
        return True
            



        
