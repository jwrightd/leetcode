class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # can track sliding window of some size, freqDict
        # take max + 2 at any given moment
        left = 0
        freq = defaultdict(int)
        mostFreq = 0
        highest = 0
        n = len(s)
        for right in range(n):
            freq[s[right]] += 1
            mostFreq = max(mostFreq, freq[s[right]])
            len_window = right - left + 1
            if len_window - mostFreq > k:
                freq[s[left]] -= 1
                left += 1
            highest = max(highest, right - left + 1)

        return highest
