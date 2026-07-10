class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # 25 mins for this theoretically

        # 115 pm

        #brute force soln is n^4
        # for a in nums1:
        # for b in nums2:
        # for c in nums3:
        # for d in nums4:
        # if a + b + c + d == 0: 
        # we have tuple (ig we need to store idx as well, so maybe we do enumerate)

        # but ok we can memoize some of this
        # can we do n^3?
        # we know we must have a number from each nums array with length n, so
        # what if put all of nums1 stuff in a set but negated
        # we do sums of other nums arrays (n^3), if the sums are in the nums1 negated set, they are valid tuples

        # ok this TLE, so let's do O(N^2) by memoizing nums1 and nums2
        #then lets store -val --> idx in a dict
        
        valIdx = {}
        for a in nums1:
            for b in nums2:
                val = -(a + b)
                if val in valIdx:
                    valIdx[val] += 1
                else:
                    valIdx[val] = 1
        
        counter = 0

        # now n2 soln
        for c in nums3:
            for d in nums4:
                if c + d in valIdx:
                    counter += valIdx[c + d]
        return counter

