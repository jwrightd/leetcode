class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # largest sum of any subarray minimized means that 
        # 7 9 14 24 32
        # k bags
        # s sum
        # then at least s/k in one bag
        # maybe just bin search for largest
        left = max(nums) # max has to be in a bag, so this is min
        right = sum(nums) # if k = 1 i guess or if we have a number > 0 and then a bunch of 0s
        best = -1

        def valid_num(mid):
            boxes = 0
            current = 0
            for n in nums:
                if current + n > mid:
                    boxes += 1
                    current = n
                else:
                    current += n
            return boxes < k
        
        while left <= right:
            mid = (left + right)//2
            if valid_num(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best

        
