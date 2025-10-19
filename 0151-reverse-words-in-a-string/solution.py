class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        p1 = 0
        p2 = len(words) - 1
        while p2 > p1:
            if words[p1] == "":
                p1 += 1
            elif words[p2] == "":
                p2 -= 1
            else:
                temp = words[p1]
                words[p1] = words[p2]
                words[p2] = temp
                p1 += 1
                p2 -=1
        w2 = [x for x in words if x != ""]
        return " ".join(w2).strip()
        """
        :type s: str
        :rtype: str
        """
        
