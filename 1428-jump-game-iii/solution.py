class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # just dfs?
        # but need to reach all 0s --- or just one? I think it's just one
        N = len(arr)
        visited = set()
        def dfs(i):
            if arr[i] == 0:
                return True
            if i in visited:
                return False
            visited.add(i)
            if i + arr[i] < N:
                if dfs(i + arr[i]):
                    return True
            if i - arr[i] >= 0:
                if dfs(i - arr[i]):
                    return True
            return False
        return dfs(start)
            
            
