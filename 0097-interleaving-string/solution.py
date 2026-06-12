class Solution(object):
    
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #some sort of dfs or bfs here
        table = dict()
        def dfs(i, j):
            k = i + j
            # we need cases for bounds
            if k == len(s3) and j == len(s2) and i == len(s1):
                return True
            elif k == len(s3):
                return False

            while not (i < len(s1) and j < len(s2) and s1[i] == s3[k] and s1[i] == s2[j]):
                if k == len(s3) and j == len(s2) and i == len(s1):
                    return True
                elif k == len(s3):
                    return False

                if i < len(s1) and s1[i] == s3[k]:
                    i += 1
                    k += 1
                elif j < len(s2) and s2[j] == s3[k]:
                    j += 1
                    k += 1
                else:
                    return False

            if i < len(s1) and j < len(s2) and s1[i] == s3[k] and s1[i] == s2[j]:
                branchone = table[(i + 1, j)] if (i + 1, j) in table else dfs(i + 1, j)
                table[(i + 1, j)] = branchone
                branchtwo = table[(i, j+ 1)] if (i, j+1) in table else dfs(i, j + 1)
                table[(i, j + 1)] = branchtwo

                return branchone or branchtwo
        return dfs(0,0)
        
