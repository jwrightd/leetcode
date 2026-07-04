class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # algo:
        # take last num count, add one
        # subtract math.log num base 2
        output = [0]
        twos = [0]
        last = 0
        for i in range(1, n + 1):
            last += 1
            if i % 2 == 0:
                last -= (twos[i//2] + 1)
                twos.append(twos[i//2] + 1)
            else:
                twos.append(0)
            output.append(last)
        return output


