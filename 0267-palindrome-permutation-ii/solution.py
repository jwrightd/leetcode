class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        oddCnt = 0
        for v in freq:
            if freq[v] % 2 == 1:
                oddCnt += 1
            if oddCnt > 1:
                return []
        
        # now we dfs it
        res = []
        def dfs(left, right, state):
            if right < left:
                res.append("".join([i for i in state]))
                return
            if right == left:
                for val in freq:
                    if freq[val] > 0:
                        state[right] = val
                        dfs(left + 1, right - 1, state)
                return 
            for val in freq:
                if freq[val] >= 2: # can choose
                    state[left] = val
                    state[right] = val
                    freq[val] -= 2
                    dfs(left + 1, right - 1, state)
                    freq[val] += 2
            return
        N = len(s)
        dfs(0, N - 1, [0 for _ in range(N)])
        return res

