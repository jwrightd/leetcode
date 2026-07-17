class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        # precompute nums --> indices:
        count = 0
        inds = {}
        for i in nums:
            if i in inds:
                inds[i].append(count)
            else:
                inds[i] = [count]
            count += 1
        n = -1 if x not in inds else len(inds[x])
        output = []
        for q in queries:
            if x not in inds:
                output.append(-1)
            else:
                if q <= n:
                    output.append(inds[x][q - 1])
                else:
                    output.append(-1)
        return output
                
