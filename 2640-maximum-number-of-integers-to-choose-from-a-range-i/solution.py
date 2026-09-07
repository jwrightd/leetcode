class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        tot = 0
        cnt = 0
        banSet = set(banned)
        for i in range(1, n + 1):
            if i in banSet:
                continue
            tot += i
            cnt += 1
            if tot > maxSum:
                return cnt - 1
        return cnt
