class Solution(object):
    def isOneBitCharacter(self, bits):
        while 1 in bits:
            bits = bits[bits.index(1) + 2:]
        return False if len(bits) == 0 else True
