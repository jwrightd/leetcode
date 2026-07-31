class Solution:
    def validPalindrome(self, s: str) -> bool:
        # algo
        # start in middle
        # move outwards until you reach ends
        # if there is a mismatch, can move oneo f the pointers
        def palindrome(a):
            return a == a[::-1]
        
        N = len(s)
        i, j = 0, N - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return palindrome(s[i + 1:j + 1]) or palindrome(s[i: j])

        return True
        #  cupcuu
