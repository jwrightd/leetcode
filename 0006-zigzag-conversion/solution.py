class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rowDict = dict()
        count = 0
        increasing = True
        for i in range(len(s)):
            if count in rowDict:
                rowDict[count].append(s[i])
            else:
                rowDict[count] = list()
                rowDict[count].append(s[i])
            count = count + 1 if increasing else count - 1
            if count == numRows:
                count -= 2
                increasing = False
            elif count == - 1:
                count += 2
                increasing = True
        s = ""
        #sor = dict(sorted(my_dict.items()))
        for i in rowDict:
            for x in rowDict[i]:
                s += x
        print(rowDict)
        return s
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
