class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # ok can sort and then set element and bin search?
        nums.sort()
        # -4 -1 1 2 tgt 1
        # set some element and then two ptr on rest?
        # on2 sol
        N = len(nums)
        closestSum = -1
        closestDist = float('inf')
        for start in range(N):
            left, right = start + 1, N - 1
            newTarget = target - nums[start]
            while left < right:
                distance = abs((nums[left] + nums[right]) - newTarget)
                if distance < closestDist:
                    closestDist, closestSum = distance, nums[left] + nums[right] + nums[start]
                if nums[left] + nums[right] < newTarget:
                    left += 1
                else:
                    right -= 1
        return closestSum


