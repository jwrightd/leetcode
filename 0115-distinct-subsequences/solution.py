class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #i think dp, either choose or dont choose for each character
        # dict with key as (s, t) modified pairs
        # return numDistinct(s[1:], t) + numDistinct(s[1:], t without that char)
        #except its not s[1:], its s at index of the first char of t
        #base case: if t is empty string

        table = dict()
        t_len = len(t)
        s_len = len(s)

        def dfs(i, j): # i is index in s, j is idx in t
            if j == t_len:
                return 1
            if i == s_len:
                return 0
            else: 
                currChar = t[j]
                if s[i] != t[j]: #then skip
                    if (i + 1, j) in table:
                        skip = table[(i + 1, j)]
                    else:
                        skip = dfs(i + 1, j)
                        table[(i + 1, j)] = skip
                    return skip
                else: 
                    if (i + 1, j + 1) in table:
                        choose = table[(i + 1, j + 1)]
                    else:
                        choose = dfs(i + 1, j + 1)
                        table[(i + 1, j + 1)] = choose
                    if (i + 1, j) in table:
                        skip = table[(i + 1, j)]
                    else:
                        skip = dfs(i + 1, j)
                        table[(i + 1, j)] = skip
                    return choose + skip
        
        return dfs(0, 0)

