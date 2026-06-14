class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #brute force is to check every possible substring
        #Backtracking?
        palindromes = []
        pDict = dict()
        def isPalindrome(phr):
            l = len(phr)
            for i in range(l//2):
                if phr[i] != phr[l - i - 1]:
                    return False
            return True
        length = len(s)

        def dfs(start, path):
            if start == len(s):
                palindromes.append([i for i in path])
                return
            
            for end in range(start + 1, length + 1):
                substring = s[start:end]

                if substring in pDict:
                    valid = pDict[substring]
                else:
                    valid = isPalindrome(substring)
                    pDict[substring] = valid

                if valid:
                    path.append(substring)
                    dfs(end, path)
                    path.pop()
        dfs(0, [])          
        return palindromes




            




