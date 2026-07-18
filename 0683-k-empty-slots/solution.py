class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        # let's just try brute force
        # we check k + 1 in both dirs when we add a new thing
        # O(N * K)
        n = len(bulbs)
        tracking = [0] * n

        day = 1
        for bulb in bulbs:
            tracking[bulb - 1] = 1
            #print(tracking)
            valid = True
            for i in range(1, k + 1):
                if bulb - 1 + i == n or tracking[bulb - 1 + i] == 1:
                    valid = False
                    break
            if valid and bulb + k < n and tracking[bulb + k] == 1:
                return day
            valid = True
            for i in range(1, k + 1):
                if bulb - 1 - i < 0 or tracking[bulb - 1 - i] == 1:
                    #print()
                    valid = False
                    break
            if valid and bulb - 2 - k >= 0 and tracking[bulb - 2 - k] == 1:
                return day
            day += 1
        return -1
            
        
        
