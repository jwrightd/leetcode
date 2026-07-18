class Solution:
    def nextClosestTime(self, time: str) -> str:
        # i think we just brute force this
        # we extract all nums
        # wait no, you can use as many times sa you want, so maybe we do greedy
        digits = sorted([time[0], time[1], time[3], time[4]])
        
        def timeDist(first, nextTime):
            gap = 0
            if nextTime < first:
                gap += 24 * 60
            
                hourDiff = int(first[:2]) - int(nextTime[:2])
                minDiff = int(first[3:]) - int(nextTime[3:])
                gap -= 60 * hourDiff
                gap -= minDiff
            else:
                hourDiff = int(nextTime[:2]) - int(first[:2])
                minDiff = int(nextTime[3:]) - int(first[3:])
                gap += 60 * hourDiff
                gap += minDiff
            return gap
        # wrong approach, we want to create the closest time to start from scratch
        # maybe we start with lowest position, we we have a num bigger than it then we swap, otherwise we keep same and go left
        # then tens, if we have a valid number there we swap
        # else we go hours units, then hours tens
        # if nothing works, then we do smallest num 4 times
        
        for i in digits:
            if i > time[4]:
                tmp = list(time)
                tmp[4] = i
                return "".join(tmp)
        
        for i in digits:
            if i > time[3] and i < "6":
                tmp = list(time)
                tmp[3] = i
                tmp[4] = digits[0]
                return "".join(tmp)
        # if we change the hour then we need to make mins small as possible
        for i in digits:
            if (i > time[1] and time[0] == "2" and i <= "3") or (i > time[1] and time[0] != "2"): 
                tmp = list(time)
                tmp[1] = i
                tmp[3] = digits[0]
                tmp[4] = digits[0]
                return "".join(tmp)
        
        for i in digits:
            if i > time[0] and i <= "2":
                tmp = list(time)
                tmp[0] = i
                #if tmp[1] >= "4":
                tmp[1] = digits[0]
                tmp[3] = digits[0]
                tmp[4] = digits[0]
                return "".join(tmp)
        
        return digits[0] + digits[0] + ":" + digits[0] + digits[0]
        
                
                
        
        
        # 18:39
        # 9 cant change, 3 fcant be replaced, 8 we can do 9
                    
                
            
        
