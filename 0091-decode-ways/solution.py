class Solution(object):
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp_table = dict()
        def recur(s):
            if len(s) == 0:
                return 1
            #feels like DP
            # go char by char
            # ex: 11106
            # take nD(1106) + nD(106)
            opt1 = int(s[0])
            opt2 = int(s[0:2]) if len(s) >= 2 else 0
            o1 = 0
            o2 = 0
            if opt1 != 0:
                if s[1:] not in dp_table:
                    o1 = recur(s[1:]) 
                    dp_table[s[1:]] = o1
                else:
                    o1 = dp_table[s[1:]]
                
            if opt2 > 9 and opt2 < 27:
                if s[2:] not in dp_table:
                    o2 = recur(s[2:]) 
                    dp_table[s[2:]] = o2
                else:
                    o2 = dp_table[s[2:]]
                #o2 = self.numDecodings(s[2:])

            return o1 + o2
        
        return recur(s)

