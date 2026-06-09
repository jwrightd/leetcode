class Solution(object):
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False
        def valid(possible_perm, s1_freq, s2_freq):
            for i in s1_freq:
                if i not in s2_freq or s1_freq[i] != s2_freq[i]:
                    return False
            return True
        
        s1_freq = dict()
        s2_freq = dict()

        for i in range(s1_len):
            if s1[i] in s1_freq:
                s1_freq[s1[i]] += 1
            else:
                s1_freq[s1[i]] = 1
            
            if s2[i] in s2_freq:
                s2_freq[s2[i]] += 1
            else:
                s2_freq[s2[i]] = 1
        #initial shit set up

        #sliding window
        start = 0
        while start + s1_len <= s2_len:
            possible = s2[start:start+s1_len]
            if valid(possible, s1_freq, s2_freq):
                return True
            if start + s1_len < s2_len:
                s2_freq[s2[start]] -= 1
                s2_freq[s2[start + s1_len]] = 1 if s2[start + s1_len] not in s2_freq else 1 + s2_freq[s2[start + s1_len]]
            start += 1
        return False
        
        
        



        
