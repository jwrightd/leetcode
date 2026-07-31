class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # need some backtracking
        # we should check number of normal char
        # match those
        # then . can by any char -- just match to next one
        # * is harder part
        # * can be any number of thing, so probably we check number of things it can match to, those are children
        # dp[i][j] is whether you can match up to i, j
        dp = {}
        N = len(s)
        M = len(p)
        def dfs(i, j):
            #print(s[i:], p[j:])
            if i == N and j == M:
                return True
            if j == M:
                return False

            if i == N and j < M: # no more cahr to match
                if j + 1 < M and p[j + 1] == "*":
                    return dfs(i, j + 2)
                return False
            
            if j + 1 < M and p[j + 1] == "*":
                prevChar = p[j]
                 
                if prevChar == ".":
                    # stuff
                    children = [idx for idx in range(i, N + 1)]
                else:
                    children = [] # to dfs for i coord
                    idx = i
                    while idx < N and s[idx] == prevChar:
                        children.append(idx)
                        idx += 1
                    children.append(idx)
                #print(prevChar, children)
                for child in children:
                    if (child, j + 2) in dp:
                        res = dp[(child, j + 2)]
                    else:
                        res = dfs(child, j + 2)
                        dp[(child, j + 2)] = res
                    if res:
                        return True
            elif s[i] == p[j] or p[j] == ".":
                if (i + 1, j + 1) in dp:
                    return dp[(i + 1, j + 1)]
                else:
                    res = dfs(i + 1, j + 1)
                    dp[(i + 1, j + 1)] = res
                    return res
       
            return False

        
        return dfs(0,0)
            
