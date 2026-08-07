class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # we do we only choose increasing nums
        output = []

        def recur(i, state):
            if len(state) == k:
                output.append([i for i in state])
            else:
                for j in range(i, n + 1):
                    if n - j < k - len(state) - 1:
                        break
                    state.append(j)
                    recur(j + 1, state)
                    state.pop(-1)

        
        recur(1, [])
        return output
