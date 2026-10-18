class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # 2ptr
        sp, tp = 0, 0
        a, b = len(s), len(t)
        numEdits = 0
        while sp < a and tp < b:
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            elif b > a:
                tp += 1
                numEdits += 1
            elif a > b:
                sp += 1
                numEdits += 1
            else:
                sp += 1
                tp += 1
                numEdits += 1
            if numEdits > 1:
                return False
        
        return (numEdits == 1 and sp == a and tp == b) or (numEdits == 0 and abs(b-a) == 1)
        
