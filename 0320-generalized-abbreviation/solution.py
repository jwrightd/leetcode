class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # ok its just choose/notchoose
        res = []
        N = len(word)
        def dfs(i, state):
            if i >= N:
                res.append("".join(state))
                return
            # our choices are as follows
            # 1. we choose the letter, i += 1
            # 2. we abbreviate some number of letters, we increase i this length and 1 more
            state.append(word[i])
            dfs(i + 1, state) # choose
            state.pop(-1)

            for r in range(1, N - i + 1):
                addition = str(r) + word[i + r] if i + r < N else str(r)
                state.append(addition)
                dfs(i + r + 1, state)
                state.pop(-1)

            return
        dfs(0, [])
        return res
