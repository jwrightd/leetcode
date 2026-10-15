# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        N = mountainArr.length()
        saved = {}
        def getPivot(mountainArr):
            l, r = 0, N - 1
            while l <= r:
                mid = (l + r)//2
                if mid == 0 or mid == N - 1:
                    return mid
                before = saved[mid - 1] if mid - 1 in saved else mountainArr.get(mid - 1)
                val = saved[mid] if mid in saved else mountainArr.get(mid)
                after = saved[mid + 1] if mid + 1 in saved else mountainArr.get(mid + 1)
                saved[mid - 1], saved[mid], saved[mid + 1] = before, val, after
                if before < val and val > after:
                    return mid
                if before < val and val < after:
                    l = mid + 1
                else:
                    r = mid - 1
        pivot = getPivot(mountainArr)
        # before is inc
        l, r = 0, pivot
        best = -1
        while l <= r:
            mid = (l + r)//2   

            val = saved[mid] if mid in saved else mountainArr.get(mid)
            saved[mid] = val

            if val == target:
                best = mid
                r = mid - 1
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        if best != -1:
            return best
        # else need to search after pivot
        l, r = pivot + 1, N - 1
        while l <= r:
            mid = (l + r)//2   

            val = saved[mid] if mid in saved else mountainArr.get(mid)
            saved[mid] = val

            if val == target:
                best = mid
                l = mid + 1
            elif val < target:
                r = mid - 1
            else:
                l = mid + 1
        return best


        


