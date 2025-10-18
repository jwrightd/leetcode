class Solution(object):
    def reverseVowels(self, s):
        listIdx = set()
        vList = []
        length = len(s)
        vowels = "aeiou"
        for i in range(length):
            if s[i].lower() in vowels:
                listIdx.add(i)
                vList.append(s[i])
        vList = vList[::-1]
        st = ""
        count = 0
        for i in range(length):
            if i in listIdx:
                st += vList[count]
                count += 1
            else:
                st += s[i]
        return st
        

        """
        :type s: str
        :rtype: str
        """
        
