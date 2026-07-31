class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        N = len(s)
        while i < N // 2:
            tmp = s[N - i - 1]
            s[N - i - 1] = s[i]
            s[i] = tmp
            i += 1
        
