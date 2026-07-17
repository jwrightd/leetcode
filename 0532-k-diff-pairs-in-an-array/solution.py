class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        visited = set()
        paired = set()
        count = 0
        for i in nums:
            if k == 0:
                if i in visited and i not in paired:
                    count = count + 1
                    paired.add(i)
                visited.add(i)
            elif i not in visited:
                visited.add(i)
                if i - k in visited:
                    count += 1
                if i + k in visited:
                    count += 1
        return count
            
