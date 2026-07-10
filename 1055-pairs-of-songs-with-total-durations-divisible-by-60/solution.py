class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # num pairs where vals at i, j have a sum that is divis by 60
        # this seems like very similar to twosum, feels like we can do this in o(n).
        # obviously brute force is o(n^2)
        # can we do o(logn)? i dont think so, if time was sorted maybed but proll ynot here
        # or maybe n is hard, if we nlogn sort
        #ohh i get it, we can do each num % 60 or something
        # 30, 20, 30, 40, 40
        valids = set()
        remainders = {}
        count = 0
        for idx, val in enumerate(time):
            rem = val % 60
            if rem in remainders:
                remainders[rem] += 1
            else:
                remainders[rem] = 1

        for i in remainders:
            tgt = 60 - i 
            if i == 0 or i == 30:
                count += (remainders[i] * (remainders[i] - 1)) //2
            elif tgt in remainders:
                count += remainders[i] * remainders[tgt]
                remainders[i] = 0
        return count  
        
