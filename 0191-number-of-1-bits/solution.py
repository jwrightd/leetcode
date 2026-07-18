class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # num set bits
        # can we check  if dvisible by 2 and then //2
        count = 0
        while n > 0:
            count = count + 1 if n % 2 else count
            n /= 2
        return count
