class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        # ok this is what im thinking:
        # we can order arr
        # we can do freq dict
        # then we do standard 3 sum soln, but we multiply by the multiplicity for all 3 nums
        # but we also want like multiplicity (so if we need a multiple of a number)
        freq = {}
        filtered = []
        for num in arr:
            if num not in freq:
                filtered.append(num)
            freq[num] = 1 if num not in freq else freq[num] + 1
        filtered.sort()
        n = len(filtered)
        ways = 0
        #print(freq)
        #print(filtered)
        for idx, a in enumerate(filtered): # need to check unique pairs
            for b in filtered[idx:]:
                c = target -a -b
                
                if c in freq and c >= a and c >= b:
                    if a == b == c: # all same
                        ways += freq[a] * (freq[a] - 1) * (freq[a] - 2) // 6
                    elif a == b: # two same
                        ways += freq[c] * freq[a] * (freq[a] - 1) // 2
                    elif a == c:
                        ways += freq[b] * freq[a] * (freq[a] - 1) // 2
                    elif b == c:
                        ways += freq[a] * freq[b] * (freq[b] - 1) // 2
                    else: # all diff
                        ways += freq[a] * freq[b] * freq[c]
                    #freq[a] = freq[b] = 0
                    #print(ways)
        return ways % (10**9 + 7)






        

        
