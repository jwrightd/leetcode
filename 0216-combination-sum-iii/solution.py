class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # we'll say that we choose in increasing order so we do combos once
        # dfs
        # ends when sum is equal to n with k elements
        valid = []
        def dfs(state):
            if len(state) == k and sum(state) == n:
                valid.append([i for i in state])
                return
            if len(state) == k:
                return
            
            if len(state) == 0: # can have anything
                for num in range(1, 10):
                    state.append(num)
                    dfs(state)
                    state.pop(-1)
            else:
                for num in range(state[-1] + 1, 10):
                    state.append(num)
                    dfs(state)
                    state.pop(-1)
            
            return
        
        dfs([])

        return valid
        
