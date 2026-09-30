class Solution(object):
    import random
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.pref = []
        for idx, val in enumerate(w):
            if idx == 0:
                self.pref.append(val)
            else:
                self.pref.append(self.pref[-1] + val)
        print(self.pref)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        size = self.pref[-1]
        tgt = random.randint(1, size)
        lower, higher = 0, len(self.pref) - 1
        best = -1
        while lower <= higher:
            
            mid = (lower + higher)//2
            #print(mid, self.pref, lower, higher)
            if self.pref[mid] == tgt:
                return mid
            if self.pref[mid] > tgt:
                higher = mid - 1
                best = mid
            else:
                lower = mid + 1
        return best
            
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
