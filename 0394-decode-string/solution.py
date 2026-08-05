class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # need to do brackets
        # recursion
        output = []
        stk = []
        idx = 0
        N = len(s)
        nums = "1234567890"
        while idx < N:
            current = s[idx]
            #print(stk)
            if current == "]":
                phr = []
                
                while stk and stk[-1] != "[":
                    phr.append(stk[-1])
                    stk.pop(-1)
                stk.pop(-1) # remove last [
                number = []
                while stk and stk[-1] in nums:
                    number.append(stk[-1])
                    stk.pop(-1)
                number = int("".join(number[::-1]))
                phr = "".join(phr[::-1])
                stk.append(phr * number)
            else:
                stk.append(current)
            idx += 1
       # print(stk)


    

        return "".join(stk) + s[idx:]


        
