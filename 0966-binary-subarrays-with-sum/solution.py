class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        # running sum - prev prefix = goal
        prefixes = {0:1}
        running_sum = 0
        numSubarrays = 0
        for i in nums:
            running_sum += i
            if running_sum - goal in prefixes:
                numSubarrays += prefixes[running_sum - goal]
            prefixes[running_sum] = 1 if running_sum not in prefixes else prefixes[running_sum] + 1
        return numSubarrays

