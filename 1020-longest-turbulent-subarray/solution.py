class Solution(object):
    def maxTurbulenceSize(self, arr):
        N = len(arr)
        if N < 3:
            return N if not (N == 2 and arr[0] == arr[1]) else N - 1
        # greedy sliding window
        current = 1 if arr[0] == arr[1] else 2
        longest = current
        for idx in range(2, N):
            if (arr[idx - 1] > arr[idx] and arr[idx - 1] > arr[idx - 2]) or (arr[idx - 1] < arr[idx] and arr[idx - 1] < arr[idx - 2]):
                current += 1
                longest = max(current, longest)
            else:
                current = 1 if arr[idx] == arr[idx - 1] else 2

        return max(longest, current)
        
