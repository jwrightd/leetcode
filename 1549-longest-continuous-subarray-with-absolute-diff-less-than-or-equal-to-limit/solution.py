class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # track big small
        import heapq

        maxHeap = []
        minHeap = []

        N = len(nums)
        longest = 0
        left = 0
        right = 0
        small, big = float('inf'), float('-inf')


        while right < N and big - small <= limit:
            heapq.heappush(maxHeap, [-nums[right], right])
            heapq.heappush(minHeap, [nums[right], right])
            small = minHeap[0][0]
            big = -maxHeap[0][0]
            if big - small <= limit:
                longest = max(longest, right - left + 1)
                right += 1
            else:
                while left < right and big - small > limit:
                    left += 1
                    while maxHeap and maxHeap[0][1] < left:
                        heapq.heappop(maxHeap)
                    while minHeap and minHeap[0][1] < left:
                        heapq.heappop(minHeap)
                    
                    small = minHeap[0][0]
                    big = -maxHeap[0][0]
           
        return longest


