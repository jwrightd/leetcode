class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n = 0 --> 0
        # n = 1 --> 1
        # n = 2 --> 1
        # n = 3 --> 1
        # n = 4 --> 2
        # primes?
        # n= 5 --> 2
        # wait no, perf squares
        # non perf squares will have canceling stuff, so we get off
        # perf squares have odd num of unique factors (9 has 1, 3, 9 for example bc 3 is repeated)
        cnt = 0
        r = 1
        while r ** 2 <= n:
            cnt += 1
            r += 1

        return cnt

