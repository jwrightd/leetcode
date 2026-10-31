class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        current = 0
        N = len(nums)
        start = None
        res = []
        if N == 0:
            return []
        while current != N:
            if start == None:
                start = current
            else:
                if current - start != nums[current] - nums[start]:
                    if current - 1 == start:
                        res.append(str(nums[start]))
                    else:
                        res.append(str(nums[start]) + "->" + str(nums[current - 1]))
                    start = None
                else:
                    current += 1
        if current - 1 == start:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[current - 1]))


        return res
