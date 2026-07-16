class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # num subarrays with k odds
        # 4 odds, 4 C 3 = 4
        # 1 2 2 3 4

        # 2 odds
        # 0, 0, 0, 1, 1, 1, 2, 2, 2, 2

        # checking all subarrays is N^2
        # checking if each subarray has K odd is N, so we get N^3
        # but maybe we can memoize each subarray

        # best approach is prefixes
        # first let's make odds 1, evens 0
        prefArr = []
        for i in nums:
            if i % 2 == 1:
                prefArr.append(1)
            else:
                prefArr.append(0)
        prefs = {0:1}
        running_sum = 0
        count = 0
        for i in prefArr:
            running_sum += i
            if running_sum - k in prefs:
                count += prefs[running_sum - k]
            prefs[running_sum] = 1 if running_sum not in prefs else prefs[running_sum] + 1
        return count
        
