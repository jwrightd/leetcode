class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        #what's our algo here
        # a letter can be in max one partition
        # we want to maximize number of partitions
        # this sounds like greedy algorithm
        # maybe we just take first and last idx of all letters
        # we sort them by start, then overlap 
        # if next start is greater than last end, we can start new partition
        N = len(s)

        def lastIdx(letter):
            last = N - 1
            while last >= 0 and s[last] != letter:
                last -= 1
            return last

        currentStart = -1
        currentEnd = -1
        output = []

        alpha = set()
        idx = 0

        while idx < N:
            letter = s[idx]
            if letter not in alpha:
                alpha.add(letter)
                start = idx
                end = lastIdx(letter)

                if start > currentEnd:
                    if currentEnd != -1:
                        output.append(currentEnd - currentStart + 1)
                    currentStart = start
                    currentEnd = end   
                elif end > currentEnd:
                    currentEnd = end
            idx += 1
        output.append(currentEnd - currentStart + 1)
        return output
                

