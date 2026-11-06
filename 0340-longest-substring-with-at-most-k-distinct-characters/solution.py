class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        numUsed = 0
        l = 0
        N = len(s)
        freq = defaultdict(int)
        longestSeq = 0

        for r in range(N):
            ch = s[r]
            freq[ch] += 1
            if freq[ch] == 1:
                numUsed += 1
            while numUsed > k:
                remove = s[l]
                freq[remove] -= 1
                if freq[remove] == 0:
                    numUsed -= 1
                l += 1
            longestSeq = max(longestSeq, r - l + 1)
        return longestSeq
            

