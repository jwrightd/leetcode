class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp to find LIS
        # increment LIS when find
        freqs = defaultdict(int)
        N = len(nums)
        counts = [1] * N    
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        counts[i] = counts[j]
                    elif dp[j] + 1 == dp[i]:
                        counts[i] += counts[j]


                    dp[i] = max(dp[i], dp[j] + 1)
        longest = max(dp)

       # print(dp, counts)
        return sum([count for length, count in zip(dp, counts) if length == longest])

