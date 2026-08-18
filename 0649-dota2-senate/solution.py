class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # this is simulation
        # always want to ban unless all are valid
        # so im thinking we have a flag for if next dire or radiant is banned/can vote next
        # if not banned, we update the string
        radiant = 0
        dire = 0
        rCount = senate.count("R")
        dCount = senate.count("D")
        
        while rCount > 0 and dCount > 0:
            nextRound = []
            idx = 0
            while idx < len(senate):
                current = senate[idx]
                if current == "R":
                    if radiant >= 0:
                        dCount -= 1
                        dire -= 1
                        nextRound.append("R")
                    else:
                        radiant += 1
                else:
                    if dire >= 0:
                        rCount -= 1
                        radiant -= 1
                        nextRound.append("D")
                    else:
                        dire += 1
                idx += 1
            senate = "".join(nextRound)
        return "Radiant" if rCount > 0 else "Dire"
            
