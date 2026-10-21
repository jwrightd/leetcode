class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = defaultdict(int)
        res = 0

        N = len(s)
        numLetters = 0
        left = 0
        for right in range(N):
            curr = s[right]
            freq[curr] += 1
            if freq[curr] == 1:
                numLetters += 1
            while numLetters > 2:
                leftChar = s[left]
                freq[leftChar] -= 1
                if freq[leftChar] == 0:
                    numLetters -= 1
                left += 1
            res = max(res, right - left + 1) 


        return res
