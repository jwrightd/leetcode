class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        N = len(nums)
        for i in nums:
            freqs[i] += 1
            if freqs[i] >= N / 2:
                return i
