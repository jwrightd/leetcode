class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            numChar = str(len(s))
            length = str(len(numChar))
            res += length + numChar + s
        return res
 
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(s)
        while i < n:
            length = int(s[i])
            numChar = int(s[i + 1:i + 1 + length])
            res.append(s[i + 1 + length : i + 1 + length + numChar])
            i += 1 + length + numChar

        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
