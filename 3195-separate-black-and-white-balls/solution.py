class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # greedy
        # want all 1s to right
        # 0s to left
        # two ptr?
        N = len(s)
        total = 0
        l, r = 0, N - 1
        while l < r:
            if s[l] == "0":
                l += 1
            elif s[r] == "1":
                r -= 1
            else: # both are wrong --> move the 1 to the right, move both ptrs
                total += (r - l)
                r -= 1
                l += 1
        return total



        return total

