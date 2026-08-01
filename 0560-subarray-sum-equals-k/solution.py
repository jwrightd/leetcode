class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # can prefix sum, then do N^2
        pref = [i for i in nums]
        N = len(pref)
        for i in range(1, N):
            pref[i] += pref[i - 1]
        count = 0
        # memo it
        freq = defaultdict(int)
        freq[0] = 1

        for idx, val in enumerate(nums):
            if pref[idx] - k in freq:
                count += freq[pref[idx] - k]
            freq[pref[idx]] += 1
        return count

