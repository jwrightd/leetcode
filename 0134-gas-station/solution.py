class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = 0
        length = len(gas)
        i = 0
        while i < length:
            move = 0
            tank = 0
            while move != length:
                tank = tank + gas[(move + i) % length] - cost[(move + i) % length]
                if tank < 0:
                    if (move + i) % length < i:
                        return -1
                    i = (move + i) % length
                    break
                move += 1
                if move == length:
                    return i
            i += 1
        return -1
            
