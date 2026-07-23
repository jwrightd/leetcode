class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        # lets memoize this, 
        # brute force is N^3, just do i, j, k loops where j starts at i + 1, k starts at j + 1
        # check condition
        # can get down to N^2 with memo, only question is if we should do N^2 memo where we store a pair of idx
        # or just one, i think one is best
        # so O(N) mem and O(N^2) soln. memoizng both would make it O(N^2) mem and O(N^2) soln since we have to do nested loops to doulbe memoize both

        # track L, R, and then track the remainders between L, R
        n = len(nums)
        output = 0
        for i in range(n):
            freqs = defaultdict(int)
            for j in range(i + 1, n): 
                needed = d - ((nums[i] + nums[j]) % d)
                #print(needed)
                
                if needed in freqs:
                    #print(i, j)
                    output += freqs[needed]
                dictKey = (nums[j] % d) if nums[j] % d != 0 else d
                freqs[dictKey] += 1
            #print(freqs)
        return output
                
                


