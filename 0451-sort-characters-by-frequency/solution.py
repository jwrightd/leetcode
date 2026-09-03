class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqs = defaultdict(int)
        for i in s:
            freqs[i] += 1
        stuff = list(s)
        stuff.sort(key=lambda x : (-freqs[x], x))
        return "".join(stuff)
        
        
