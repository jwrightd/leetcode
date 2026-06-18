class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #treat all indices as middle idx and expand
        #need case for both odd and even length
        length = len(s)
        counter = 0
        for i in range(length):
            left = i
            right = i + 1
            #even case
            while right < length and left >= 0 and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
            #odd case
            left = i
            right = i
            while right < length and left >= 0 and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1
        return counter
        
