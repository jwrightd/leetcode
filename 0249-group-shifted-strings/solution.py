class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        alpha = "abcdefghijklmnopqrstuvwxyz"
        def shift(s):
            res = []
            for char in s:
                scale_0_25 = ord(char) - ord('a')
                shifted_scale = (scale_0_25 + 1) % 26
                new_char = chr(shifted_scale + ord('a'))
                res.append(new_char)
                
            return "".join(res)

        
        unique = defaultdict(list)

        for s in strings:
            tmp = s
            found = False
            for _ in range(26):
                tmp = shift(tmp)
                if tmp in unique:
                    unique[tmp].append(s)
                    found = True
                    break
            if not found:
                unique[s] = [s]
                
            

        res = []
        for i in unique:
            res.append(unique[i])
        return res
