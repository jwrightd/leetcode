class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # want highest digits first
        # so sort, revesre = True
        # then just join?
        if nums.count(0) == len(nums):
           return "0"
        def comp(a, b):
            return -1 if (a + b) > (b + a) else 1
        strNums = [str(i) for i in nums]
        strNums.sort(key=cmp_to_key(comp))
        return "".join(strNums)
        
