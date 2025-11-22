class Solution(object):
    def minimumOperations(self, nums):
        return sum([1 for i in nums if i%3 != 0])
        
