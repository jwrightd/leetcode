class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        N = len(nums)
        output = []
        def recur(i, state):
            if i == N:
                output.append([i for i in state])
            else:
                for num in freq:
                    if freq[num] > 0:
                        freq[num] -= 1
                        state.append(num)
                        recur(i + 1, state)
                        state.pop(-1)
                        freq[num] += 1
                        
        recur(0, [])
        return output

        
