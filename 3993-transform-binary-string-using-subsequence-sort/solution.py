class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        ans = []
        # ok i think we deal with the ? first
        # maybe just throw it all into a set?
        # so i think it doesnt actually matter, we just need the right number of 1 and 0
        # you can always swap a 1 backwards with a 0, so we should just make the last few ? -> 1, rest 0
        
        for possible in strs:
            n = len(possible)
            numQ = possible.count("?")
            numOnes = s.count("1") - possible.count("1")
            tmp = list(possible)
            idx = n - 1
            while idx >= 0 and numOnes > 0:
                if tmp[idx] == "?":
                    tmp[idx] = "1"
                    numOnes -= 1
                idx -= 1
            for idx, val in enumerate(tmp):
                if tmp[idx] == "?":
                    tmp[idx] = "0"
            if numOnes != 0:
                ans.append(False)
                continue
            curated = "".join(tmp)
            nOnePoss = 0
            valid = True
            for idx in range(n):
                if s[idx] == "1":
                    nOnePoss += 1
                if curated[idx] == "1":
                    nOnePoss -= 1
                if nOnePoss < 0:
                    valid = False
                    break
        
            if not valid:
                ans.append(False)
            elif numOnes == 0:
                ans.append(True)
                    
            #print("".join(tmp))
        return ans
                
            
