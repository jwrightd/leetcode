class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = dict()
        for i in strs:
            lStr = list(i)
            lStr.sort()
            newStr = "".join(lStr)
            if newStr in anagrams:
                anagrams[newStr].append(i)
            else:
                anagrams[newStr] = []
                anagrams[newStr].append(i)
        ret = []
        for i in anagrams:
            ret.append(anagrams[i])
        return ret


