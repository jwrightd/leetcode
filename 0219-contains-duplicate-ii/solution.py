class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # sliding window hashmap
        n = len(nums)
        freq = defaultdict(int)
        for i in range(min(k + 1, n)):
            freq[nums[i]] += 1
            if freq[nums[i]] > 1:
                return True
        
        for i in range(k + 1, n):
            freq[nums[i - k - 1]] -= 1
            freq[nums[i]] += 1
            if freq[nums[i]] > 1:
                return True
 
        return False
            
        
