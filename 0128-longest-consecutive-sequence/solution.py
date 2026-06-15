class Solution(object):
    import heapq
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #pq?
        #heapify is o(n)
        heapq.heapify(nums)
        #num is heap
        highest = 0
        current = 0
        lastNum = None
        while len(nums) > 0:
            curr = heapq.heappop(nums)
            if lastNum == None or curr - lastNum == 1:
                lastNum = curr
                current += 1
            elif curr - lastNum == 0:
                lastNum = curr
            else:
                highest = current if current > highest else highest
                current = 1
                lastNum = curr
        highest = current if current > highest else highest
        return highest

        
