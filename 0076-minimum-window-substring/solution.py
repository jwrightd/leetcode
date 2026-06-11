class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #sliding window

        # make dict for t
        t_letters = dict()
        length = len(t)
        lenS = len(s)

        for i in range(len(t)):
            t_letters[t[i]] = 1 + t_letters[t[i]] if t[i] in t_letters else 1

        window = dict()
        minimumWindow = ""
        k = len(s)
        count = 0

        l = 0
        r = 0
        while r < len(s):
            #expand
            while r < len(s) and count < length:
                curr = s[r]
                window[curr] = 1 if curr not in window else window[curr] + 1
                if curr in t_letters and window[curr] <= t_letters[curr]:
                    count += 1
                r += 1
            #contract
            while count == length:
                curr = s[l]
                window[curr] -= 1
                if curr in t_letters and window[curr] < t_letters[curr]:
                    # save the stuff
                    count -= 1
                    if r - l <= k:
                        k = r - l 
                        minimumWindow = s[l:r]
                    
                l += 1

        return minimumWindow

        

