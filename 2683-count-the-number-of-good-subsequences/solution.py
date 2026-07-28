class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        # seems like a math question
        # because this is a subsequence question, it is just choose combinatorics
        # we want a freq dict
        # we want to count cases where we have an diff number of any letter
        #
        # a:2, b:2
        # -> a = 1, b: 2Ci from i = 1 to n, but skip when i = 1
        # -> a = 2, b: 2Ci from i = 1 to n, but skip when i = 2

        # easier to check # of good
        MOD = 10 ** 9 + 7
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1

        n = len(s)
        maxFreq = max(freq.values())

        factorials = [1] * (maxFreq + 1)
        factorials[0] = 1
        for i in range(1, maxFreq + 1):
            factorials[i] = i * factorials[i - 1] % MOD

        inverse_factorials = [1] * (maxFreq + 1)
        inverse_factorials[maxFreq] = pow(factorials[maxFreq], MOD - 2, MOD)

        for i in range(maxFreq, 0, -1):
            inverse_factorials[i - 1] = i * inverse_factorials[i] % MOD
        count = 0

        def getCount(i): #nCr = n!/( (n - r)! r! ) but also we need to choose num of items to include
            mult = 1
            
            for item in freq:
                if freq[item] >= i:
                    #mult *= (1 + math.comb(freq[item], i)) # + 1 choice for not including the number
                    mult *= (1 + factorials[freq[item]] * inverse_factorials[i] * inverse_factorials[freq[item] - i])


    
            return int(mult - 1) if mult > 1 else 0 # subtract 1 to ignore empty subsequence
            
        for i in range(1, n + 1): # all chars happen i times
            res= getCount(i)
            count += res
            
        return count % (10**9 + 7)
            

        
        

