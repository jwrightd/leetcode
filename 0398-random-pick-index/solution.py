class Solution(object):
    import random
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.map = defaultdict(list)
        for idx, val in enumerate(nums):
            self.map[val].append(idx)
        


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return self.map[target][random.randint(0, len(self.map[target]) - 1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
