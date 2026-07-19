class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        # same color is even, wrong color is odd
        return True if ((target[0] + target[1]) - (start[0] + start[1])) % 2 == 0 else False
